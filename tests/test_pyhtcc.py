'''
includes all tests for PyHTCC
'''
import pathlib
import sys
import unittest.mock

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from pyhtcc import PyHTCC, Zone, AuthenticationError, TooManyAttemptsError


class TestPyHTCC(object):
    def setup(self):
        with unittest.mock.patch('pyhtcc.pyhtcc.requests.session') as mock_session:
            self.mock_session = mock_session
            self.mock_session.return_value = self.mock_session

            result = unittest.mock.MagicMock()
            result.status_code = 200
            # make 12345 our location_id
            result.url = 'portal/12345/'
            self.mock_post_result(result)
            self.pyhtcc = PyHTCC('user', 'pass')

            assert self.pyhtcc._locationId == 12345

    def mock_post_result(self, result):
        self.next_requests_result = result
        self.mock_session.post.return_value = self.next_requests_result

    def mock_get_result(self, result):
        self.next_requests_result = result
        self.mock_session.get.return_value = self.next_requests_result

    def test_submitting_raw_control_changes_will_raise_keyerror_on_invalid_keys(self):
        with pytest.raises(KeyError):
            self.pyhtcc.submit_raw_control_changes(0, {
                'KewlDown' : 1
            })

    def test_submitting_raw_control_changes_will_raise_valueerror_on_success_not_being_1(self):
        result = unittest.mock.Mock()
        result.json = lambda: { 'success' : 0 }

        self.mock_post_result(result)
        with pytest.raises(ValueError):
            self.pyhtcc.submit_raw_control_changes(0, {})

    def test_getting_outdoor_weather_for_zone(self):
        result = unittest.mock.Mock()
        # put data in that is part of the actual response that we care about
        result.text = '''        Control.Model.set(Control.Model.Property.isInVacationHoldMode, false);
        Control.Model.set(Control.Model.Property.outdoorHumidity, 47);
        Control.Model.set(Control.Model.Property.outdoorTemp, 74);
        Control.Model.set(Control.Model.Property.schedCoolSp, 78);'''
        self.mock_get_result(result)

        info = self.pyhtcc._get_outdoor_weather_info_for_zone(0)
        assert info == {
            'OutdoorTemperature' : 74,
            'OutdoorHumidity' : 47,
        }

    def test_getting_outdoor_weather_for_zone_no_temp(self):
        result = unittest.mock.Mock()
        # put data in that is part of the actual response that we care about
        result.text = '''        Control.Model.set(Control.Model.Property.isInVacationHoldMode, false);
        Control.Model.set(Control.Model.Property.outdoorHumidity, 47);
        Control.Model.set(Control.Model.Property.schedCoolSp, 78);'''
        self.mock_get_result(result)

        info = self.pyhtcc._get_outdoor_weather_info_for_zone(0)
        assert info == {
            'OutdoorTemperature' : None,
            'OutdoorHumidity' : 47,
        }

    def test_getting_outdoor_weather_for_zone_no_humidity(self):
        result = unittest.mock.Mock()
        # put data in that is part of the actual response that we care about
        result.text = '''        Control.Model.set(Control.Model.Property.isInVacationHoldMode, false);
        Control.Model.set(Control.Model.Property.outdoorTemp, 74);
        Control.Model.set(Control.Model.Property.schedCoolSp, 78);'''
        self.mock_get_result(result)

        info = self.pyhtcc._get_outdoor_weather_info_for_zone(0)
        assert info == {
            'OutdoorTemperature' : 74,
            'OutdoorHumidity' : None,
        }

    def test_get_name_for_device_id(self):
        result = unittest.mock.Mock()
        result.text = '''<div class="TitleAndAlerts">

            <div id="ControlScreenHeader">
                <h1 id="ZoneName">DOWNSTAIRS Control</h1>
            </div>

            <div id="AlertsPlaceHolder">

        </div>
        '''
        self.mock_get_result(result)
        assert self.pyhtcc._get_name_for_device_id(0) == 'DOWNSTAIRS'

        # now we're cached
        self.mock_get_result(None)
        assert self.pyhtcc._get_name_for_device_id(0) == 'DOWNSTAIRS'

        # trying a different id would error since it would try to get w/o using the cache (and get a None object back)
        with pytest.raises(AttributeError):
            assert self.pyhtcc._get_name_for_device_id(1) == 'DOWNSTAIRS'

    def test_authentication_can_fail_eventually(self):
        def _raise():
            _raise.count += 1
            raise TooManyAttemptsError
        self.pyhtcc._do_authenticate = _raise
        _raise.count = 0

        with pytest.raises(AuthenticationError):
            with unittest.mock.patch('pyhtcc.pyhtcc.time.sleep'):
                self.pyhtcc.authenticate()

        assert _raise.count == 100



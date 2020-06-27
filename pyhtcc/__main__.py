'''
A cli entry point to do quick calls to PyHTCC
'''
import argparse
import os
import pprint

from .pyhtcc import PyHTCC, Zone, enableConsoleLogging

def main():
    parser = argparse.ArgumentParser(description='A CLI to perform actions on a Honeywell Total Comfort Connect thermostat system')
    parser.add_argument('-u', '--user', type=str, help='Username to login to TCC. If not given uses the environment variable PYHTCC_EMAIL')
    parser.add_argument('-p', '--password', type=str, help='Password to login to TCC. If not given uses the environment variable PYHTCC_PASS')
    parser.add_argument('-n', '--name', type=str, help='Thermostat name to target. If not given, targets all zones')
    parser.add_argument('-s', '--show-info', action='store_true', help='If given, will show info and quit.')
    parser.add_argument('-d', '--debug', action='store_true', help='If given, will log to stdout')
    args = parser.parse_args()

    if args.debug:
        enableConsoleLogging()

    if args.user:
        user = args.user
    else:
        if 'PYHTCC_EMAIL' in os.environ:
            user = os.environ['PYHTCC_EMAIL']
        else:
            raise ValueError("Must provide -u/--user or have environment variable PYHTCC_EMAIL set")

    if args.password:
        password = args.password
    else:
        if 'PYHTCC_PASS' in os.environ:
            password = os.environ['PYHTCC_PASS']
        else:
            raise ValueError("Must provide -up--password or have environment variable PYHTCC_PASS set")

    pyhtcc = PyHTCC(user, password)

    if args.name:
        zones = [pyhtcc.get_zone_by_name(args.name)]
    else:
        zones = pyhtcc.get_all_zones()

    if args.show_info:
        for i in zones:
            pprint.pprint(i.zone_info)

if __name__ == '__main__':
    main()

[![Run tests and release](https://github.com/csm10495/pyhtcc/actions/workflows/test_and_release.yml/badge.svg)](https://github.com/csm10495/pyhtcc/actions/workflows/test_and_release.yml) ![PyPI Version](https://img.shields.io/pypi/v/pyhtcc?color=green)

# PyHTCC

An (unofficial) library for interfacing with a Honeywell Total Connect Comfort (TCC) thermostat system. It includes both a simple CLI and an API.

# Installation
```
pip install pyhtcc
```

# Simple API Example
```
from pyhtcc import PyHTCC
p = PyHTCC(<TCC username>, <TCC password>)
zone = p.get_zone_by_name('<zone name>')

# set cooling on, and a setpoint of 75 degrees
zone.set_permanent_cool_setpoint(75)
```
See [https://csm10495.github.io/pyhtcc/](https://csm10495.github.io/pyhtcc/) for full API documentation.

## Multi-location accounts

For TCC accounts that have more than one location (for example, two
thermostats configured under separate "locations" in the TCC portal),
login picks the first location id as the active one and exposes the
full sorted list on `client.location_ids`. To work with a different
location, set `_locationId` before any per-location call:

```
p = PyHTCC(<TCC username>, <TCC password>)
print(p.location_ids)        # e.g. [3532155, 3532164]

# Work with location 3532164's zones:
p._locationId = 3532164
zones = p.get_all_zones()
```

# CLI Syntax

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./help_output.txt) -->
<!-- The below code snippet is automatically added from ./help_output.txt -->
```txt
usage: pyhtcc [-h] [-u USER] [-p PASSWORD] [-n NAME] [-s] [-d] [-l]
              [-H HEAT | -C COOL]

A CLI to perform actions on a Honeywell Total Comfort Connect thermostat
system

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  Username to login to TCC. If not given uses the
                        environment variable PYHTCC_EMAIL
  -p PASSWORD, --password PASSWORD
                        Password to login to TCC. If not given uses the
                        environment variable PYHTCC_PASS. If neither are
                        given, will prompt for user input.
  -n NAME, --name NAME  Thermostat name to target. If not given, targets all
                        zones
  -s, --show-info       If given, will show info and quit.
  -d, --debug           If given, will log to stdout
  -l, --logout          if given, will logout from TCC after performing
                        actions.
  -H HEAT, --heat HEAT  Set a target heat temperature
  -C COOL, --cool COOL  Set a target cooling temperature
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## License
MIT License

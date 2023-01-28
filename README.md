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

# CLI Syntax

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./help_output.txt) -->
<!-- The below code snippet is automatically added from ./help_output.txt -->
```txt
usage: pyhtcc [-h] [-u USER] [-p PASSWORD] [-n NAME] [-s] [-d]
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
  -H HEAT, --heat HEAT  Set a target heat temperature
  -C COOL, --cool COOL  Set a target cooling temperature
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## License
MIT License

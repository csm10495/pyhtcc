# PyHTCC

An (unofficial) library for interfacing with a Honeywell Total Connect Comfort (TCC) thermostat system. It includes both a simple CLI and an API.
See [https://csm10495.github.io/pyhtcc/](https://csm10495.github.io/pyhtcc/) for API documentation.

# Installation
```
pip install pyhtcc
```

# CLI Syntax


[CLI_OUTPUT_MARKER]::

usage: pyhtcc [-h] [-u USER] [-p PASSWORD] [-n NAME] [-s] [-d]
              [-H HEAT | -C COOL]

A CLI to perform actions on a Honeywell Total Comfort Connect thermostat
system

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Username to login to TCC. If not given uses the
                        environment variable PYHTCC_EMAIL
  -p PASSWORD, --password PASSWORD
                        Password to login to TCC. If not given uses the
                        environment variable PYHTCC_PASS
  -n NAME, --name NAME  Thermostat name to target. If not given, targets all
                        zones
  -s, --show-info       If given, will show info and quit.
  -d, --debug           If given, will log to stdout
  -H HEAT, --heat HEAT  Set a target heat temperature
  -C COOL, --cool COOL  Set a target cooling temperature

[CLI_OUTPUT_MARKER]::


## License
MIT License
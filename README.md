![Run tests](https://github.com/csm10495/pyhtcc/workflows/Run%20tests/badge.svg) [![PyPI version](https://badge.fury.io/py/pyhtcc.svg)](https://badge.fury.io/py/pyhtcc)

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

<!-- MARKDOWN-AUTO-DOCS:END -->

## License
MIT License

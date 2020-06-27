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
zone.set_permananent_cool_setpoint(75)
```
See [https://csm10495.github.io/pyhtcc/](https://csm10495.github.io/pyhtcc/) for full API documentation.

# CLI Syntax

[CLI_OUTPUT_MARKER]::

[CLI_OUTPUT_MARKER]::

## License
MIT License
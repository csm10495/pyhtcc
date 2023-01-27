"""
A cli entry point to do quick calls to PyHTCC
"""
import argparse
import getpass
import os
import pprint

from csmlog import enableConsoleLogging

from pyhtcc import PyHTCC


def main():
    parser = argparse.ArgumentParser(
        "pyhtcc",
        description="A CLI to perform actions on a Honeywell Total Comfort Connect thermostat system",
    )
    parser.add_argument(
        "-u",
        "--user",
        type=str,
        help="Username to login to TCC. If not given uses the environment variable PYHTCC_EMAIL",
    )
    parser.add_argument(
        "-p",
        "--password",
        type=str,
        help="Password to login to TCC. If not given uses the environment variable PYHTCC_PASS. If neither are given, will prompt for user input.",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Thermostat name to target. If not given, targets all zones",
    )
    parser.add_argument(
        "-s",
        "--show-info",
        action="store_true",
        help="If given, will show info and quit.",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="If given, will log to stdout"
    )

    heat_cool_action_group = parser.add_mutually_exclusive_group(required=False)
    heat_cool_action_group.add_argument(
        "-H", "--heat", type=int, help="Set a target heat temperature"
    )
    heat_cool_action_group.add_argument(
        "-C", "--cool", type=int, help="Set a target cooling temperature"
    )
    args = parser.parse_args()

    if args.debug:
        enableConsoleLogging()

    if args.user:
        user = args.user
    else:
        if "PYHTCC_EMAIL" in os.environ:
            user = os.environ["PYHTCC_EMAIL"]
        else:
            raise ValueError(
                "Must provide -u/--user or have environment variable PYHTCC_EMAIL set"
            )

    if args.password:
        password = args.password
    else:
        if "PYHTCC_PASS" in os.environ:
            password = os.environ["PYHTCC_PASS"]
        else:
            password = getpass.getpass(f"Password ({user}): ")

    pyhtcc = PyHTCC(user, password)

    if args.name:
        zones = [pyhtcc.get_zone_by_name(args.name)]
    else:
        zones = pyhtcc.get_all_zones()

        for i in zones:
            if args.show_info:
                pprint.pprint(i.zone_info)

            if args.heat:
                print(f"Setting setpoint for {i.get_name()} to {args.heat}")
                i.set_permanent_heat_setpoint(args.heat)

            if args.cool:
                print(f"Setting setpoint for {i.get_name()} to {args.cool}")
                i.set_permanent_cool_setpoint(args.cool)


if __name__ == "__main__":
    main()

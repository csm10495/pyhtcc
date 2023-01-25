"""
script to create docs
"""

import os
import re
import shutil
import subprocess
import sys

if __name__ == "__main__":
    assert (
        subprocess.call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "setuptools",
                "pdoc3",
            ]
        )
        == 0
    ), "Unable to install pdoc3"

    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    assert (
        subprocess.call(
            [sys.executable, "-m", "pdoc", "--html", "pyhtcc", "-o", "docs_tmp", "-f"]
        )
        == 0
    ), "Unable to generate docs via pdoc"

    # remove existing docs dir
    shutil.rmtree("docs", ignore_errors=True)

    # remove extra dir nesting and move back to docs/
    shutil.move("docs_tmp/pyhtcc", "docs")
    os.rmdir("docs_tmp")

    help_output = subprocess.check_output(
        sys.executable + " -m pyhtcc --help", shell=True
    ).decode()

    with open("README.md", "r") as f:
        readme_txt = f.read()

    CLI_MARKER = "[CLI_OUTPUT_MARKER]::"

    pre_cli_help, _, post_cli_help = readme_txt.split(CLI_MARKER)

    new_readme = (
        pre_cli_help
        + "\n"
        + CLI_MARKER
        + "\n\n```\n"
        + help_output
        + "\n```\n"
        + CLI_MARKER
        + "\n"
        + post_cli_help
    )

    # try to remove excess empty lines
    new_readme = new_readme.replace("\r\n", "\n")
    while "\n\n\n" in new_readme:
        new_readme = new_readme.replace("\n\n\n", "\n\n")

    with open("README.md", "w") as f:
        f.write(new_readme)

'''
script to create docs
'''

import os
import subprocess
import sys

if __name__ == '__main__':
    assert subprocess.call([
        sys.executable,
        '-m',
        'pip',
        'install',
        'pdoc3',
    ]) == 0, 'Unable to install pdoc3'

    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    assert subprocess.call([
        sys.executable,
        '-m',
        'pdoc',
        '--html',
        'pyhtcc',
        '-o',
        'docs',
        '-f'
    ]) == 0, 'Unable to generate docs via pdoc'

'''
Brief:
    Quick script to build this and upload it to pypi.
Author(s):
    Charles Machalow
'''

import os
import shutil
import subprocess
import sys

THIS_FOLDER = os.path.realpath(os.path.dirname(__file__))
DIST_FOLDER = os.path.join(THIS_FOLDER, 'dist')

def caller(c):
    print ('Calling: %s' % c)
    subprocess.call(c, shell=True)

# delete dist folder
try:
    shutil.rmtree(DIST_FOLDER)
except:
    pass # doesn't exist


caller('\"%s\" -m pip install twine' % sys.executable)

os.chdir(THIS_FOLDER)
caller('\"%s\" setup.py sdist' % sys.executable)

for file in os.listdir(DIST_FOLDER):
    if file.upper().endswith('.TAR.GZ'):
        break

caller('\"%s\" -m twine upload \"dist/%s\" -r pypi' % (sys.executable, file))
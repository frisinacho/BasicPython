__author__ = 'Nacho'

import subprocess

subprocess.call(['ls', '-l'])

for i in range(0, 10):
    nameDir = "dir" + str(i)
    subprocess.call(['mkdir', nameDir])

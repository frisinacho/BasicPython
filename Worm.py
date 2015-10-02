__author__ = 'Nacho'

from sys import argv
import subprocess

script = argv
name = str(script[0])
print name

for i in range(0, 10):
    directory = 'dir' + str(i)
    subprocess.call(['mkdir', directory])
    subprocess.call(['cp', name, directory])

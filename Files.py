__author__ = 'Nacho'

from sys import argv

script, filename = argv

print "Creating %r file" % filename

file = open(filename, 'w')
file.write("This file is a test")
file.close()

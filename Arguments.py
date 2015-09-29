__author__ = 'Nacho'

from sys import argv

script, name, lastName = argv

print "Hello %s %s" % (name, lastName)  # cmd> python Arguments.py Name LastName

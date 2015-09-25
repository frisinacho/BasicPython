__author__ = 'Nacho'

import math

# Factorial
print math.factorial(4)

# Log
print math.log1p(2.4)

# More stuff
print "Give me a number:"
num = float(raw_input())

factorial = math.factorial(math.floor(num))
logarithm = math.log1p(num)

print "The log of %f is %f and its factorial is %d" % (num, logarithm, factorial)

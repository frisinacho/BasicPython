__author__ = 'Nacho'

for index in "Hello world!":
    print index

# For with lists
names = ["Jorge", "Carlos", "Denis"]

for name in names:
    print "The current name is:"
    print name

# Range
for count in range(0, 10):
    print count

# Length
name = "Jorge"

for count in range(len(name)):
    print count
    print name[count]

print ""
print "-----------"
print ""

# While loop
count = 0
while count < 20:
    print "The counter is %d" % count
    count += 1

__author__ = 'Nacho'


class Dog:
    legs = 4
    name = ""

    def naming(self, n):
        self.name = n

pet = Dog()
pet.naming("Lola")

print "I've a dog, it's name is %s and have %s legs" % (pet.name, pet.legs)

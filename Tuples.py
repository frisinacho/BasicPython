__author__ = 'Nacho'

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print my_list[0]  # 1
print my_tuple[0]  # 1

my_list[0] = 10  # 10
my_tuple[0] = 10  # ERROR

my_list.sort()

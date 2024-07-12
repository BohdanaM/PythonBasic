import random

my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print("Initial list of random numbers:", my_list)

new_list = [my_list[0], my_list[2], my_list[-2]]
print("New list with selected items:", new_list)

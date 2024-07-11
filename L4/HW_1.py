lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zeros_quantity = lst.count(0)
new_lst = []

for el in lst:
    if el != 0:
        new_lst.append(el)
new_lst += [0] * zeros_quantity
print(new_lst)

lst = [0, 1, 7, 2, 4, 8]
new_lst = []

for el in lst:
    if lst.index(el) % 2 == 0:
        new_lst.append(el)
sum_of_even_num = (sum(new_lst))

if len(lst) < 1:
    result = 0
else:
    last_element = lst[-1]
    result = sum_of_even_num * last_element
print(result)

lst = [1, 2, 3, 4, 5, 6]

if len(lst) % 2 == 0:
    middle_index = len(lst) // 2
    first_list = lst[:middle_index]
    second_list = lst[middle_index:]
    new_list = [first_list, second_list]
    print(new_list)
else:
    middle_index = (len(lst) // 2) + 1
    first_list = lst[:middle_index]
    second_list = lst[middle_index:]
    new_list = [first_list, second_list]
    print(new_list)

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


# my_list = [1, 2, 3]
#
# half = len(my_list) // 2
# if len(my_list) % 2 == 0:
#     result = my_list[:half], my_list[half:]
# else:
#     result = ((my_list[:half + 1]), (my_list[half:]) * 0 + my_list[half + 1:])
# print(result)

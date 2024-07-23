def common_elements():
    # Generating a list of numbers that are multiples of 3
    list_multiple_3 = [num for num in range(0, 101) if num % 3 == 0]

    # Generating a list of numbers that are multiples of 5
    list_multiple_5 = [num for num in range(0, 101) if num % 5 == 0]

    # Changing lists into sets
    set_list_multiple_3 = set(list_multiple_3)
    set_list_multiple_5 = set(list_multiple_5)

    # Finding the intersection of the sets
    intersection_set = set_list_multiple_3 & set_list_multiple_5

    return intersection_set


result = common_elements()
print("Common elements:", result)

def add_one(some_list):
    # Convert list to string
    string_number = "".join([str(el) for el in some_list])

    # Convert string to number and find sum
    result_number = int(string_number) + 1

    # Convert result_number to list
    numbers_list = [int(num) for num in str(result_number)]

    return numbers_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")

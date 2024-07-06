lst = [12, 3, 4, 10, 8]

if len(lst) <= 1:
    print(lst)  # when list will be empty or consist 1 element
else:
    last_element = lst[-1]
    lst.pop()
    lst.insert(0, last_element)
    print(lst)

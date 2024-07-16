# import string
# import keyword
#
# variable = input("Enter a name of variable:")
# #Check that the variable starts with a number
# if variable[0].isdigit():
#     result = False
# Check that the variable has capital letters
# elif any(char.isupper() for char in variable):
#     result = False
# # Check that the variable has punctuation marks except the underscore "_".
# elif any(char in string.punctuation.replace('_', '') for char in variable):
#     result = False
# # Check that the variable has a space
# elif ' ' in variable:
#     result = False
# # Check that the variable has keywords Python
# elif variable in keyword.kwlist:
#     result = False
# # Check that the variable has more than 1 underscore "_"
# elif variable.count('__') > 0:
#     result = False
# else:
#     result = True
# print(result)

import keyword
import string

variable = input("Enter a name of variable:")

result = (
        not variable[0].isdigit()
        and not any(char.isupper() for char in variable)
        and not any(char in string.punctuation.replace("_", "") for char in variable)
        and " " not in variable
        and variable not in keyword.kwlist
        and variable.count("__") <= 0
)

print(result)

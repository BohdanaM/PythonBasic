number = int(input("Enter an integer: "))

while number > 9:
    result = 1
    # Iterate over each digit of the number until the number will be = 0
    while number > 0:
        digit = number % 10  # Find last number
        result *= digit  # Multiply the previous result by a digit
        number //= 10  # Find the number that remains to continue the iteration until the number will be = 0

    number = result  # Assigning the obtained result to number to continue the iteration until the number will be <= 9

print(number)

while True:
    first_operand = float(input("Enter first digit: "))
    operator = input("Enter operator (+, -, *, /): ")
    second_operand = float(input("Enter second digit: "))

    if operator == "+":
        result = first_operand + second_operand
    elif operator == "-":
        result = first_operand - second_operand
    elif operator == "*":
        result = first_operand * second_operand
    elif operator == "/":
        if second_operand == 0:
            result = None
            print("Can not be divided by 0")
        else:
            result = first_operand / second_operand
    else:
        result = None
        print("Entered no valid data")

    print(result)

    answer = str(input("Do you want to continue?").lower())

    if answer == "yes" or answer == "y":
        continue
    else:
        print("The end")
        break

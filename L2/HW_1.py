number = int(input("Enter a 4-digit number:"))

thousands = number // 1000  # Getting the thousands digit
hundreds = (number // 100) % 10  # Getting the hundreds digit
tens = (number // 10) % 10  # Getting the tens digit
units = number % 10  # Getting the units digit

# Printing each digit in a column
print(thousands)
print(hundreds)
print(tens)
print(units)

number = int(input("Enter a 5-digit number: "))

ten_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

# Creating a new number from these numbers in the reverse order
reverse_number = (
    units * 10000 + tens * 1000 + hundreds * 100 + thousands * 10 + ten_thousands
)

# Printing reverse number
print(reverse_number)

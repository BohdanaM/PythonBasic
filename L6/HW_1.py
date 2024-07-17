import string

letters = input("Enter letters:")

# Find the first and the last letters
letters_pair = letters.split("-")
first_letter = letters_pair[0]
last_letter = letters_pair[-1]

# Find index of the first and the last letters in string.ascii_letters
start_index = string.ascii_letters.index(first_letter)
end_index = string.ascii_letters.index(last_letter)

# Find missing letters between letters_pair
new_letters = string.ascii_letters[start_index:end_index + 1]

print(new_letters)

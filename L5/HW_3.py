import string

input_words = input("Enter a string:")

# Every words starts with upper letter
words = input_words.title()

# Check that words doesn't have any symbols of set string.punctuation and spaces
checks_words = ""
for char in words:
    if char not in string.punctuation and char != " ":
        checks_words += char

# Add # to the checks_words
hashtag = "#" + "".join(checks_words)

# Cut to 140 symbol if length of finish hashtag > 140
max_length = 140
if len(hashtag) > max_length:
    hashtag = hashtag[:max_length]

print("Finish hashtag:", hashtag)

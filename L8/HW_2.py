import string


def is_palindrome(text):
    text = [char for char in text if char not in string.punctuation]
    cleaned_text = "".join(text).lower().replace(" ", "")
    reverse_text = cleaned_text[::-1]

    return cleaned_text == reverse_text


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")

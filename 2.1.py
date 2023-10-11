def is_palindrome(text):
    text = text.lower()
    text = ''.join(e for e in text if e.isalnum())

    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False
    return True


print(is_palindrome("топот"))
print(is_palindrome("привет"))
print(is_palindrome("А роза упала на лапу Азора"))

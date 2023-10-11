text = 'Never look back'
char_count = {}

for char in text:
    if char.isalnum():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print(char_count)
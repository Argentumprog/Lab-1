vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonants = "бвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ"

vowel_count = 0
consonant_count = 0
vowel_letters = []

text = input("Введите текст: ")

words = text.split()
word_count = len(words)

for letter in text:
    if letter in vowels:
        vowel_count += 1
        vowel_letters.append(letter)
    elif letter in consonants:
        consonant_count += 1

print(f"Количество гласных букв: ", vowel_count)
print(f"Количество согласных букв: ", consonant_count)
print(f"Количество слов: ", word_count)

if vowel_count == consonant_count:
    print("Гласные буквы в тексте: " + " ".join(vowel_letters))

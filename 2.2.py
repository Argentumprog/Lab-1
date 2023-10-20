def process_input(data):
    if isinstance(data, tuple):
        word_length = sum(len(word) for word in data)
        return f"Длина всех слов в кортеже: {word_length}"
    elif isinstance(data, list):
        words_count = sum(1 for item in data if isinstance(item, str) and item.isalpha())
        digit_count = sum(1 for item in data if isinstance(item, int))
        return f"Количество слов: {words_count}, Количество чисел: {digit_count}"
    elif isinstance(data, int):
        digit_count = sum(1 for digit in str(data) if int(digit) % 2 != 0)
        return f"Количество нечётных цифр: {digit_count}"
    elif isinstance(data, str):
        letter_count = sum(1 for char in data if char.isalpha())
        return f"Количество букв: {letter_count}"
    else:
        return "Неподдерживаемый тип данных"


print(process_input(("apple", "banana", "cherry")))
print(process_input(["apple", 123, "banana", 456, "cherry"]))
print(process_input(13579))
print(process_input("Hello, World!"))

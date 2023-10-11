def is_pr(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")
        return

    if start >= end:
        print("Начало диапазона должно быть меньше конца диапазона.")
        return

    print(f"Простые числа в диапазоне от {start} до {end}:")
    for number in range(start, end + 1):
        if is_pr(number):
            print(number)


main()
try:
    num = int(input("Введите число: "))
    result = 10 / num
except ValueError:
    print("Ошибка: Введите число")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль")
else:
    print(f"Результат: ", result)
finally:
    print("Завершение программы")
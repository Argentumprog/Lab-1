class Calculator:
    num1 = 1
    num2 = 1

    def input_numbers(self):
        try:
            self.num1 = float(input("Введите первое число: "))
            self.num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числа.")
            self.input_numbers()

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Деление на ноль недопустимо.")
            return None

calculator=Calculator()
calculator.input_numbers()

result_sum = calculator.add()
result_diff = calculator.subtract()
result_prod = calculator.multiply()
result_div = calculator.divide()

print(f"Сумма: {result_sum}")
print(f"Разность: {result_diff}")
print(f"Произведение: {result_prod}")
print(f"Частное: {result_div}")
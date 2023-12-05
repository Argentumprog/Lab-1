import numpy as np
import matplotlib.pyplot as plt

def y(x, a):
    return np.sin(x/3) + 1.2 * a

x = 3.567
a = np.arange(-5, 12, 2.5)
y = y(x, a)
print(y)
print("Наибольшее значение: ", np.max(y))
print("Наименьшее значение: ", np.min(y))
print("Срeднее значение: ", np.mean(y))
print("Количество элементов массива: ", len(y))

plt.plot(a, y, marker='o', label='y(x)')
plt.plot(a, np.full_like(a, np.mean(y)), marker='s', label='Среднее значение')

plt.xlabel('a')
plt.ylabel('y')
plt.title('График функции y(a)')
plt.legend()

plt.show()
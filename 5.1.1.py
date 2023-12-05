import numpy as np

x = 1.59

y = (np.sin(np.pi / 6) + (3 + x ** 2) ** 0.5 - (np.log10(x - 1)) ** 3) / np.arcsin(x / 2)

print(y)
import numpy as np

N = 1
X = np.column_stack((np.ones(12), np.random.randint(N, N+12, 12), np.random.randint(60, 82, 12)))

Y = np.random.uniform(13.5, 18.6,12)


A = (np.linalg.inv((X.transpose()).dot(X))).dot((X.transpose()).dot(Y))

Y2 = X.dot(A)

print("оценки коэф \n", A)
print("исходные значения \n", Y)
print("полученные значения\n",Y2)
matr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

n = len(matr)
for i in range(n):
    for j in range(n):
        if i == j:
            matr[i][j] = 1
        elif i < j:
            matr[i][j] = 0
        else:
            matr[i][j] = 2

for row in matr:
    print(row)

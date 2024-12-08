import numpy as np

data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
matrix = np.zeros((n, n), dtype=np.int32)

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix[i] = row

kernel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
kernel_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

gra_x = np.zeros_like(matrix)
gra_y = np.zeros_like(matrix)

for i in range(1, n - 1):
    for j in range(1, n - 1):
        re = matrix[i - 1:i + 2, j - 1:j + 2]
        gra_x[i][j] = np.sum(re * kernel_x)
        gra_y[i][j] = np.sum(re * kernel_y)

edge = np.sqrt(gra_x ** 2 + gra_y ** 2)

for row in edge:
    for i in row:
        print(int(i), end=' ')
    print()

import numpy as np
import cv2

data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
matrix = np.zeros((n, n), dtype=np.uint8)
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix[i] = row

laplace_ma = cv2.Laplacian(matrix, cv2.CV_64F)
result = np.uint8(np.absolute(laplace_ma))

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()
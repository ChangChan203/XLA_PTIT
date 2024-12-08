import numpy as np


def isodata_threshold(matrix, epsilon=0.001):
    matrix = np.array(matrix)

    hist, bins = np.histogram(matrix.flatten(), bins=np.arange(257))
    p = hist / hist.sum()

    t0 = 4.5

    while True:
        group_0 = np.where(matrix < t0)
        group_1 = np.where(matrix >= t0)

        mean_0 = np.mean(matrix[group_0]) if len(group_0[0]) > 0 else 0
        mean_1 = np.mean(matrix[group_1]) if len(group_1[0]) > 0 else 0

        t = (mean_0 + mean_1) / 2
        if abs(t - t0) < epsilon:
            break

        t0 = t
    return int(np.round(t))


data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

threshold = isodata_threshold(matrix)
print(f"Isodata threshold = {threshold}")
import numpy as np


def otsu_thresholding(m):
    hist, bins = np.histogram(m.flatten(), bins=256, range=[0, 256])
    total_pixels = m.size
    sum_all = np.sum(np.arange(256) * hist)

    weight_b = 0
    sum_b = 0
    max_var_between = 0
    optimal_threshold = 0

    for i in range(256):
        weight_f = total_pixels - weight_b

        if weight_b > 0 and weight_f > 0:
            mean_b = sum_b / weight_b
            mean_f = (sum_all - sum_b) / weight_f
            var_between = weight_b * weight_f * (mean_b - mean_f) ** 2

            if var_between > max_var_between:
                max_var_between = var_between
                optimal_threshold = i
        weight_b += hist[i]
        sum_b += i * hist[i]
    return optimal_threshold


data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
m = []
for i in range(n):
    row = [int(j) for j in input().split()]
    m.append(row)

m = np.array(m)
threshold = otsu_thresholding(m) - 1

print(f"Otsu threshold = {threshold}")
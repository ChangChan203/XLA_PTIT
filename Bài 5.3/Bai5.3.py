import cv2
import numpy as np

rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

gray_image = np.array(matrix, dtype=np.uint8)

smoothed_3 = cv2.blur(gray_image, (3, 3))
smoothed_5 = cv2.blur(gray_image, (5, 5))

print("\nLược đồ xám đã làm trơn (w=3):")
for row in smoothed_3:
    for i in row:
        print(i, end=' ')
    print()

print("\nLược đồ xám đã làm trơn (w=5):")
for row in smoothed_5:
    for i in row:
        print(i, end=' ')
    print()

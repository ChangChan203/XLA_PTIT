import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../BTL/Chapter 1/Algr 1.1/image/cycle.jpg', cv2.IMREAD_GRAYSCALE)

# Tính gradient sử dụng Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Ngưỡng hóa tại 99.7 percentile
threshold_value = np.percentile(gradient_magnitude, 99.7)
mask = (gradient_magnitude > threshold_value).astype(np.uint8) * 255

# Nhân ảnh nhiễu với mask
result_image = cv2.bitwise_and(image, image, mask=mask)

# Lọc các pixel khác không
nonzero_pixels = result_image[result_image > 0]

# Áp dụng ngưỡng Otsu dựa trên lược đồ xám trong (e)
# Dùng Otsu để tìm ngưỡng
_, otsu_threshold = cv2.threshold(result_image, 0, 255,
                                  cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tạo figure với 3 hàng và 2 cột để hiển thị 6 ảnh
plt.figure(figsize=(18, 12))

# (a) Ảnh nhiễu
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.axis('off')

# (b) Lược đồ xám của ảnh nhiễu
plt.subplot(2, 3, 2)
plt.hist(image.ravel(), bins=256, range=[0, 256], color='black')

# (c) Mask image formed from gradient threshold
plt.subplot(2, 3, 3)
plt.imshow(mask, cmap='gray')
plt.axis('off')

# (d) Image formed as product of (a) and (c)
plt.subplot(2, 3, 4)
plt.imshow(result_image, cmap='gray')
plt.axis('off')

# (e) Lược đồ xám của các pixel khác không trong ảnh (d)
plt.subplot(2, 3, 5)
plt.hist(nonzero_pixels.ravel(), bins=256, range=[0, 256], color='black')

# (f) Kết quả phân ngưỡng Otsu
plt.subplot(2, 3, 6)
plt.imshow(otsu_threshold, cmap='gray')
plt.axis('off')

# Hiển thị tất cả các ảnh cùng lúc
plt.tight_layout()
plt.show()

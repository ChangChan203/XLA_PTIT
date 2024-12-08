import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

plt.figure(figsize=(10,5))

# Hiển thị ảnh gốc
plt.subplot(1, 2, 1)
plt.title('Ảnh gốc')
plt.imshow(image, cmap='gray')
plt.axis('off')

# Hiển thị ảnh sau khi cân bằng lược đồ
plt.subplot(1, 2, 2)
plt.title('Ảnh sau cân bằng lược đồ')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()

import cv2
import numpy as np


def enhance_image(image):
    enhanced_im = image.copy()

    enhanced_im[np.where((image >= 0) & (image <= 32))] \
        = enhanced_im[np.where((image >= 0) & (image <= 32))] / 3

    enhanced_im[np.where((image > 32) & (image <= 224))] \
        = enhanced_im[np.where((image > 32) & (image <= 224))] * 3 - 2

    enhanced_im[np.where((image > 224) & (image <= 255))] \
        = enhanced_im[np.where((image > 224) & (image <= 255))] / 3 + 96

    return enhanced_im.astype(np.uint8)


def main():
    image = cv2.imread('Bai2.1.tif', cv2.IMREAD_GRAYSCALE)
    enhanced_im = enhance_image(image)
    cv2.imwrite('Bai2.1a.tif', enhanced_im)


if __name__ == '__main__':
    main()

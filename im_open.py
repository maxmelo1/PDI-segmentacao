import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('teste.jpg',0)


cv2.imshow('image',img)

#64 bit needs the mask
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

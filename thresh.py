import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('teste.jpg',0)
ori = cv2.imread('teste.jpg')
oriRGB = cv2.cvtColor(ori, cv2.COLOR_BGR2RGB)

print img.shape

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5 )
ori = cv2.resize(ori, (0,0), fx=0.5, fy=0.5 )

(width, height) =  img.shape

#print img.item(10,10)

for i in range(0, width ):
	for j in range(0, height):
		if img.item(i,j) < 127:
			img.itemset((i,j),0)
		else:
			img.itemset((i,j),255)



imgRGB = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

#cv2.imshow('image',img)
plt.subplot(121),plt.imshow(oriRGB),plt.title('Input')
plt.subplot(122),plt.imshow(imgRGB),plt.title('Output')
plt.show()

#64 bit needs the mask
if cv2.waitKey(0) & 0xFF == ord('q'):
	plt.close('all')
	cv2.destroyAllWindows()

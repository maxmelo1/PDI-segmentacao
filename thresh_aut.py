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

ret,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


imgRGB = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

images = [ oriRGB, imgRGB ]

for i in xrange(2):
	plt.subplot(1,2,i+1),plt.imshow(images[i]),plt.title('thresh')
plt.show()

#64 bit needs the mask
if cv2.waitKey(0) & 0xFF == ord('q'):
	plt.close('all')
	cv2.destroyAllWindows()

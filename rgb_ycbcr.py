import numpy as np
import cv2
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt


img = cv2.imread('teste.jpg')
imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
res = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2BGR)
imgBGR = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)


#coluna 50, linha 50
(Y, Cb, Cr) = imgYCC[50,50]
print "Cor do pixel Cb em YCbCr[50,50] = %d" % (Cb)
print "Cor do pixel Cr em YCbCr[50,50] = %d" % (Cr)


plt.imshow(imgBGR, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


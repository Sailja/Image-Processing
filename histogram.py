import numpy as np
from cv2 import * #Import functions from OpenCV
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('lego.tif',0)
hist=[0]*256
for y in range(0,img.shape[0]):
    for x in range(0,img.shape[1]):
	hist[img[y][x]]+=1
for i in range(256):
	hist[i]=hist[i]/(img.shape[0]*img.shape[1]*1.0)		
#print(hist)
plt.plot(hist)
plt.xlim([0,256])
plt.show()

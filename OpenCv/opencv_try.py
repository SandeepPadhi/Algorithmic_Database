import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 
import numpy as np
from matplotlib import pyplot as plt


#Blending images
img1 = cv2.imread('sudoku.jpeg')[:720,:720]
img1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imshow('try',img1)
cv2.waitKey(0)  
cv2.destroyAllWindows()

"""
img2 = cv2.imread('Sandeep.jpeg')[:720,:720]
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img2thresh=cv2.adaptiveThreshold(img2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)

img1bg=cv2.bitwise_and(img1,img1,mask=img2thresh)
img2thresh_not=cv2.bitwise_not(img2thresh)
img2_fg=cv2.bitwise_and(img2,img2,img2thresh_not)
result_image=cv2.add(img1bg,img2_fg)
cv2.imshow('try',result_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()
"""

"""
imgresult=cv2.addWeighted(img1,0.7,img2,0.3,0)


img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img1, 125, 255, cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(img2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 121, 1)
print(retval)
print(threshold.shape)
#print(retval.shape)
cv2.imshow('try',thresh)

#waits for user to press any key  
#(this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)  
  
#closing all open windows  
cv2.destroyAllWindows()
"""
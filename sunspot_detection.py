import os
import cv2 # opencv library
import numpy as np
import matplotlib.pyplot as plt

"""Make the pwd implementation"""
cwd = os.getcwd()
file = "\sunspot1.jpg"
path = cwd + file
#path = r'C://Users//Ditmar//python_projects//sunspot_detection//sunspot1.jpg'
image = cv2.imread(path,0)

image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#plt.show()

#plot the image in graycolor
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#plt.imshow(gray)
#plt.show()


# perform image thresholding
ret, thresh = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY)
plt.imshow(thresh, cmap = 'gray')
plt.show()


# circle = cv2.circle(thresh, (249,249),(238),(0, 255, 0),1)
# plt.imshow(circle)
# plt.show()

# find contours
contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
valid_cntrs = []

for i,cntr in enumerate(contours):
    x,y,w,h = cv2.boundingRect(cntr)
    #print("x = ",x,"y = ",y,"w = ",w,"h = ",h)
    if ((x-249)**2 + (y-249)**2)<= 238**2:
        valid_cntrs.append(cntr)
"""implement image size detection for the contur LINE 36"""

# count the number of dicovered sunspots
print("The number of sunspots is: ",len(valid_cntrs))

contour_sizes = [(cv2.contourArea(contour), contour) for contour in valid_cntrs]

for i in range(len(valid_cntrs)):
    x,y,w,h = cv2.boundingRect(contour_sizes[i][1])
    final = cv2.rectangle(image_1,(x,y),(x+w,y+h),(0,255,0),1)

plt.imshow(final)
plt.show()

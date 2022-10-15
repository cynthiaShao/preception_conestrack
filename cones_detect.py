#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import imutils
from matplotlib import pyplot as plt
import numpy as np
import pandas
plt.rcParams['figure.figsize'] = 5, 7


# In[2]:


#read the png file by file mane and convert the png to BGR
path = r"red.png"
img = cv2.imread(path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()


# In[3]:


#convert the png to HSV to detect red color
img_HSV = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
plt.imshow(img_HSV)
plt.show()


# In[4]:


#dectect "red" part from the png by setting the low and high color scale
img_thresh_low = cv2.inRange(img_HSV, np.array([0, 135, 135]), np.array([0, 255, 255])) #всё что входит в "левый красный"
img_thresh_high = cv2.inRange(img_HSV, np.array([159, 135, 135]), np.array([179, 255, 255])) #всё что входит в "правый красный"
img_thresh = cv2.bitwise_or(img_thresh_low, img_thresh_high)

plt.imshow(img_thresh)
plt.show()


# In[5]:


kernel = np.ones((6, 6))
img_thresh_opened = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)

plt.imshow(img_thresh_opened)
plt.show()


# In[6]:


img_thresh_blurred = cv2.medianBlur(img_thresh_opened, 5)
plt.imshow(img_thresh_blurred)
plt.show()


# In[7]:


#cv2.Canny(image, T_lower, T_upper)
#T_lower: Lower threshold value in Hysteresis Thresholding
#T_upper: Upper threshold value in Hysteresis Thresholding
img_edges = cv2.Canny(img_thresh_blurred, 80, 160)
plt.imshow(img_edges)
plt.show()


# In[8]:


#find the contour of the each detected pre_cones
contours = cv2.findContours(np.array(img_edges), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)


# In[9]:


#determine whether rhe detected pattern is a cone
def cones_detect(image):
    #the array of turning points that occur above the center of each pattern and below the center of each pattern
    points_above_center, points_below_center = [], []
    
    x, y, wide, height = cv2.boundingRect(image)
    #the ratio between the wide and the height of the pattern
    ratio = wide / height 
    #if the ratio is larger than 0.95, the pattern is not considered to be a cone since it's too fat
    if ratio <=0.95:
        vertical_center = y + height / 2
        for point in image:
            #check whether if every points are above or below the vertical center instead of on the vertical center line
            if point[0][1] < vertical_center:  
                points_above_center.append(point)
            elif point[0][1] >= vertical_center:
                points_below_center.append(point)
        #determine whether the upper line part of the pattern is shorter that the bottom line part of the pattern
        left_x = points_below_center[0][0][0]
        right_x = points_below_center[0][0][0]
        for point in points_below_center:
            if point[0][0] < left_x:
                left_x = point[0][0]
            if point[0][0] > right_x:
                right_x = point[0][0]

        for point in points_above_center:
            if (point[0][0] < left_x) or (point[0][0] > right_x):
                return False
    else:
        return False
        
    return True


# In[10]:


#detect the cones and put the cones in to a array
cones = []
bounding_rects = []
for image in cnts:
    if cones_detect(image):
        cones.append(image)
        rect = cv2.boundingRect(image)
        bounding_rects.append(image)


# In[11]:


#return an array of zeros with the same pattern and type as a array.
img_cones = np.zeros_like(img_edges)
#draw contour od each detected cones
cv2.drawContours(img_cones, cones, -1, (255,255,255), 2)
plt.imshow(img_cones)
plt.show()
cones_contours = cv2.findContours(np.array(img_cones), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
new_cnts = imutils.grab_contours(cones_contours)


# In[12]:


centers = []
for c in new_cnts:
    #find the center of each cone
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
# draw the center of each cone
# cv2.drawContours(img_cones, [c], -1, (0, 255, 0), 2)
# cv2.circle(img_cones, (cX, cY), 7, (255, 255, 255), -1)
# cv2.putText(img_cones, "center", (cX - 20, cY - 20),
# cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
# # show the image with cones' center
# cv2.imshow("Image of cone centers", img_cones)
# cv2.waitKey(0)
    centers.append((cX, cY))
centers = sorted(centers, key=lambda tup: tup[0])

cts = np.int32(centers)
#connect the center of each cones
cv2.polylines(img, [cts], True, (0, 0, 255), 2, cv2.LINE_AA)  
cv2.imwrite('false_answer.png',img)


# In[ ]:





# In[ ]:





# In[ ]:





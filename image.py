import sys

from PIL import Image
image_fullpath=sys.argv[1]
image_name=sys.argv[2]
img= Image.open(str(image_fullpath))
image_save_path=image_fullpath.replace(image_name,“temp.png“)
img.rotate(90).convert(“LA“).save(image_save_path)
print(“/media/temp.png“)
#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries

import numpy as np
#from numpy.lib.polynomial import poly

import matplotlib.pyplot as plt

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


# In[2]:


#loading and view the object

image = cv2.imread(r'C:\Users\HP\OneDrive\Desktop\Me\Concetto\Images\coin_counting_Image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')


# In[3]:


#creating the boxes arround various object

box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)

output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
plt.imshow(output, cmap='gray')


# In[4]:


#counting objects in the image

print("number of coins in image is : " + str(len(label)))


# In[ ]:





# In[ ]:





# In[5]:


#loading and view the object

image = cv2.imread(r'C:\Users\HP\OneDrive\Desktop\Me\Concetto\Images\count_cars.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')


# In[6]:


#creating the boxes arround various object

box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)

output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
plt.imshow(output, cmap='gray')


# In[7]:


#counting objects in the image

print("number of cars in image is : " + str(len(label)))


# In[ ]:





# In[ ]:





# In[8]:


#loading and view the object

image = cv2.imread(r'C:\Users\HP\OneDrive\Desktop\Me\Concetto\Images\count_more_cars.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')


# In[9]:


#creating the boxes arround various object

box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)

output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
plt.imshow(output, cmap='gray')


# In[10]:


#counting objects in the image

print("number of cars in image is : " + str(len(label)))


# In[ ]:

# In[1]:Import the packages
# Reg no : 
# Name : 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image, Convert to grayscale and remove noise
image1=cv2.imread ('downloads.jpg') 
gray = cv2.cvtColor
plt.title('GRAY IMAGE')
plt.imshow(gray,cmap = 'gray')

# SOBEL EDGE DETECTOR
img = cv2.Gaussian(,(3,3),0)
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel
sobelxy =cv2.Sobel()
plt.figure(1)
plt.subplot(2,2,1)
plt.imshow(gray,cmap = 'gray')
plt.title('Original'), plt.xticks([]), )

plt.subplot(2,2,2)
plt.imshow(sobelx,cmap='gray')
plt.title('sobelx')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,
plt.subplot(2,2,4)
plt.imshow(sobelxy,cmap='gray')


# In[2]:LAPLACIAN EDGE DETECTOR
laplacian = cv2.Laplacian(gray,cv2.CV_64F)
plt.imshow()
plt.title('laplacian')
plt.show()


# In[3]: CANNY EDGE DETECTOR
canny_edges = cv2.Canny(gray, 110, 140)






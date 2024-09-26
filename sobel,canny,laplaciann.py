import cv2
import matplotlib.pyplot as plt

//TYPE THE CODE HERE TO READ THE IMAGE UISNG IMREAD 
gray=cv2.cvtColor(img,)//CONVERT THE COLOR TO GRAY TO RGB
gray = cv2.GaussianBlur(gray,(3,3),0)

sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(gray)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(sobelx)
plt.title("Sobel X axis")
plt.axis("off")
plt.show()

sobely = cv2.Sobel()//TYPE THE CODE HERE 
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(gray)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(sobely)
plt.title("Sobel Y axis")
plt.axis("off")
plt.show()

sobelxy = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(gray)
plt.title("Original Image")
plt.axis("off")
//TYPE THE CODE HERE
plt.imshow(sobelxy)
plt.title("Sobel XY axis")
plt.axis("off")
plt.show()

lap=cv2.Laplacian(gray,cv2.CV_64F)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(gray)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
//DISPLAY THE IMAGE USING IMSHOW 
plt.title("Laplacian Edge Detector")
plt.axis("off")
plt.show()

canny=cv2.Canny(gray,120,150)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(gray)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(canny)
//PROVIDE THE TITLE OF THE IMAGE DISPLAYED PAGE
plt.axis("off")
plt.show()

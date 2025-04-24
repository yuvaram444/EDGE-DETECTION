# EDGE-DETECTION
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale

### Step4:
Using Sobel operator from cv2,detect the edges of the image.

### Step5:

Using Laplacian operator from cv2,detect the edges of the image and Using Canny operator from cv2,detect the edges of the image.

### Program : 
(i) Display the original image
```
import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread("C:/Users/admin/OneDrive/Pictures/Screenshots/dragon.png")  # Replace with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Display Original Image
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.show()
```
(ii) Apply Sobel Edge Detection
```
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)  # Sobel in x direction
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)  # Sobel in y direction
sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # Combine both directions
# Display Sobel Edge Detection
plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')
plt.show()
```
(iii) Apply Laplacian Edge Detection
```
# Apply Laplacian edge detector
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
# Display Laplacian Edge Detection
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Edge Detection')
plt.axis('off')
plt.show()
```
(iv) Apply Canny Edge Detection
```
canny_edges = cv2.Canny(gray_image, 50, 150)
# Display Canny Edge Detection
plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')
plt.show()
```
## Output:
### ORIGINAL IMAGE
![Screenshot 2025-04-24 094040](https://github.com/user-attachments/assets/29c2303c-94c3-4214-861f-114ec4135d82)


### SOBEL EDGE DETECTOR

![Screenshot 2025-04-24 094049](https://github.com/user-attachments/assets/e51e4b14-f9c3-4a90-9f60-39b839096a02)


### LAPLACIAN EDGE DETECTOR

![Screenshot 2025-04-24 094100](https://github.com/user-attachments/assets/dd5ebba4-c018-42c0-90cd-f70b18e0f139)


### CANNY EDGE DETECTOR
![Screenshot 2025-04-24 094110](https://github.com/user-attachments/assets/3f379286-2730-43f6-a0a9-4a3d67abb80c)


## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.

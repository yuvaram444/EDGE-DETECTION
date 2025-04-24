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
### ORIGINAL GRAY IMAGE
![Screenshot 2025-04-24 164750](https://github.com/user-attachments/assets/93a2194d-9ed8-4e2f-b5dd-c3fd0cb879e8)


### SOBEL EDGE DETECTOR

![Screenshot 2025-04-24 164800](https://github.com/user-attachments/assets/b24391d6-2082-4f6f-90da-5bd1779d9ec2)


### LAPLACIAN EDGE DETECTOR

![Screenshot 2025-04-24 164810](https://github.com/user-attachments/assets/b93a961a-472d-4236-a4b1-7c0663ebb3e4)


### CANNY EDGE DETECTOR

![Screenshot 2025-04-24 164820](https://github.com/user-attachments/assets/aa09f855-9ce3-4db9-a8cf-857a11450520)

## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.

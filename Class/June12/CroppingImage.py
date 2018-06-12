import cv2
img=cv2.imread('C:\\Users\\Lenovo\\Desktop\\Resized_demo.jpg')
cropped = img[50:500,100:500]
cv2.imshow('img',cropped)
cv2.waitKey(0)

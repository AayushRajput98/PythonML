import cv2
img=cv2.imread("F:\\pictures\\mussoorie trip\\IMG_3715.jpg")
r=800.0/img.shape[1]
dim = (700, int(img.shape[0] * r))
resized=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized",resized)
k=cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("C:\\Users\\Lenovo\\Desktop\\Resized_demo.jpg",resized)
    cv2.destroyAllWindows()
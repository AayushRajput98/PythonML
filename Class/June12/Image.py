import cv2,numpy as np
img=cv2.imread("F:\\pictures\\about\\demo.jpg")
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite("F:\\pictures\\about\\demo21.jpg", img)
    cv2.destroyAllWindows()
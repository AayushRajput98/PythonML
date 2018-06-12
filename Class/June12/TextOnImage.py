import numpy as np, cv2
from matplotlib import pyplot as plt
img=cv2.imread("F:\\pictures\\mussoorie trip\\IMG_3715.jpg")
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello! This is Aayush Rajput',(20,300), font, 1, (0,0,0), 2)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()


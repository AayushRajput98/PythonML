import numpy as np, cv2
from matplotlib import pyplot as plt
img=cv2.imread("F:\\pictures\\about\\demo.jpg")
plt.imshow(img, cmap='gray')
plt.xticks([]),plt.yticks([])   #to hide the tick values
plt.show()
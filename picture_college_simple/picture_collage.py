import numpy as np
import cv2

img1 = cv2.imread("Trojans/1_Adenta Rubian Qiyas Syahwidi.jpg")
img2 = cv2.imread("Trojans/2_Agung Maulana Putra.jpg")
img3 = cv2.imread("Trojans/3_Aidil Yusuf Priadi.jpg")

img1 = cv2.resize(img1,(200,300))
img2 = cv2.resize(img2,(200,300))
img3 = cv2.resize(img3,(200,300))

h_stack1 = np.hstack([img1, img2, img3])
h_stack2 = np.hstack([img1, img2, img3])
h_stack3 = np.hstack([img1, img2, img3])

v_stack = np.vstack([h_stack1, h_stack2, h_stack3])

cv2.imshow("collage", v_stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
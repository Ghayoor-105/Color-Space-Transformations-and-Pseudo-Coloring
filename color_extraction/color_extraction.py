import cv2
import numpy as np
img = cv2.imread("input.jpg")
b, g, r = cv2.split(img)
zeros = np.zeros_like(r)
red = cv2.merge([zeros, zeros, r])
cv2.imshow("Original", img)
cv2.imshow("Red Extracted", red)
cv2.waitKey(0)
cv2.destroyAllWindows()

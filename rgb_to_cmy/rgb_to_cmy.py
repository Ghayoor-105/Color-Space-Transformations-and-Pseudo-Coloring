import cv2
img = cv2.imread("input.jpg")
cmy = 255 - img
cv2.imshow("RGB", img)
cv2.imshow("CMY", cmy)
cv2.waitKey(0)
cv2.destroyAllWindows()

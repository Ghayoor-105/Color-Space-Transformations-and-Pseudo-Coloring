import cv2
cmy = cv2.imread("input.jpg")
rgb = 255 - cmy
cv2.imshow("CMY", cmy)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

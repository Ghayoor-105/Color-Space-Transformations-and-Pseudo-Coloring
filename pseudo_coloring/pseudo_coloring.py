import cv2
gray = cv2.imread("input.jpg", 0)
pseudo = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
cv2.imshow("Gray", gray)
cv2.imshow("Pseudo Color", pseudo)
cv2.waitKey(0)
cv2.destroyAllWindows()

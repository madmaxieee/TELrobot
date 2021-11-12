import cv2
import numpy as np

image = cv2.imread("./image1.jpg")
image = cv2.resize(image, (756, 1008), interpolation=cv2.INTER_AREA)

lower = np.array([12, -20, -21])
upper = np.array([52, 80, 79])

filtered = cv2.inRange(image, lower, upper)

# cv2.imshow("Image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

blurred = cv2.GaussianBlur(filtered, (15, 15), 0)

# find contours in the image
# print(len(cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)))
cnts, _ = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cnts) > 0:

	cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

	# compute the (rotated) bounding box around then
	# contour and then draw it
	rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
	cv2.drawContours(image, [rect], -1, (0, 255, 0), 2)

cv2.imshow("Tracking", image)
cv2.waitKey(0)
import cv2
import numpy as np

def findMask(hsv_img):
    lower_red_0 = np.array([40, 70, 0]) 
    upper_red_0 = np.array([80, 255, 255])
    lower_red_1 = np.array([40, 70, 0]) 
    upper_red_1 = np.array([80, 255, 255])
    red_mask0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
    red_mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
    red_mask = cv2.bitwise_or(red_mask0, red_mask1)

    return red_mask

kernel = np.ones((2,2),np.uint8)
img = cv2.imread('./R.jpg')
img = cv2.resize(img, (403, 302), interpolation=cv2.INTER_AREA)
print(img.shape)
blurred = cv2.pyrMeanShiftFiltering(img, 3, 3)
hsv_img = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
# red hsv range and mask on hsv_img
red_mask = findMask(hsv_img)
# print(red_mask.shape)
(contour_contours, contour_h) = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour_i = red_mask.copy()
contour_i = cv2.cvtColor(contour_i, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_i, contour_contours, -1, (0, 0, 255), 2)

avg_x = []
avg_y = []
print(len(contour_contours))
for cnt in contour_contours:
  for c in cnt:
    avg_x.append(c[0][0])
    avg_y.append(c[0][1])
print(np.mean(avg_x))
print(np.mean(avg_y))
cv2.circle(contour_i, (int(np.mean(avg_x)), int(np.mean(avg_y))), 10, (255,255,0), -1)
cv2.imshow("test_center", contour_i)
cv2.imwrite("test_center.jpg", contour_i)
cv2.waitKey(0)

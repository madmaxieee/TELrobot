import cv2
import numpy as np

def findMask(hsv_img):
    lower_red_0 = np.array([0, 70, 0]) 
    upper_red_0 = np.array([5, 255, 255])
    lower_red_1 = np.array([175, 70, 0]) 
    upper_red_1 = np.array([180, 255, 255])
    red_mask0 = cv2.inRange(hsv_img, lower_red_0, upper_red_0)
    red_mask1 = cv2.inRange(hsv_img, lower_red_1, upper_red_1)
    red_mask = cv2.bitwise_or(red_mask0, red_mask1)

    return red_mask

kernel = np.ones((2,2),np.uint8)
img = cv2.imread('./R.jpg')
img = cv2.resize(img, (403, 302), interpolation=cv2.INTER_AREA)
print(img.shape)
blurred = cv2.pyrMeanShiftFiltering(img, 5, 5)
hsv_img = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
# red hsv range and mask on hsv_img
red_mask = findMask(hsv_img)
dilation = cv2.dilate(red_mask,kernel,iterations = 2)

closing = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

#Getting the edge of morphology
edge = cv2.Canny(closing, 105, 105)
# _, contours,hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

(contour_contours, contour_h) = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour_i = red_mask.copy()
contour_i = cv2.cvtColor(contour_i, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_i, contour_contours, -1, (0, 0, 255), 2)

areas = [cv2.contourArea(c) for c in contour_contours]
print(areas)

temp = sorted(areas)[-5]
print(temp)
for i, element in enumerate(areas):
    if element >= temp:
        idx = i
        break

avg_x = []
avg_y = []
print(len(contour_contours))
for cnt in contour_contours[i:i+5]:
  for c in cnt:
    avg_x.append(c[0][0])
    avg_y.append(c[0][1])
print(np.mean(avg_x))
print(np.mean(avg_y))

cv2.circle(contour_i, (int(np.mean(avg_x)), int(np.mean(avg_y))), 5, (255,255,0), -1)
cv2.imshow("test_center", contour_i)
cv2.imwrite("test_center.jpg", contour_i)
cv2.waitKey(0)

import cv2
import numpy as np
from config import params

color_range = {
    'red0': [[0, 70, 0], [5, 255, 255]],
    'red1': [[175, 70, 0], [180, 255, 255]],
    'yellow': [[25, 70, 0], [30, 255, 255]],
    'green': [[40, 70, 0], [80, 255, 255]],
    'blue': [[100, 70, 0], [125, 255, 255]]
}


def findMask(hsv_img, color):
    if color == 'red':
        lower0, upper0 = color_range['red0']
        lower1, upper1 = color_range['red1']
        mask0 = cv2.inRange(hsv_img, lower0, upper0)
        mask1 = cv2.inRange(hsv_img, lower1, upper1)
        mask = cv2.bitwise_or(mask0, mask1)
    else:
        lower, upper = color_range[color]
        mask = cv2.inRange(hsv_img, lower, upper)

    return mask

# TODO return false if no door is found
def findDoorCenter(bgr_img, color) -> tuple:
    kernel = np.ones((2, 2), np.uint8)

    x_size, y_size = params['cam_size']
    bgr_img = cv2.resize(bgr_img, (x_size/2, y_size/2),
                         interpolation=cv2.INTER_AREA)

    blurred = cv2.pyrMeanShiftFiltering(bgr_img, 5, 5)
    hsv_img = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = findMask(hsv_img, color)
    dilation = cv2.dilate(mask, kernel, iterations=2)

    closing = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    # Getting the edge of morphology
    edge = cv2.Canny(closing, 105, 105)
    # _, contours,hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    (contour_contours, _) = cv2.findContours(
        edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contour_i = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_i, contour_contours, -1, (0, 0, 255), 2)

    areas = [cv2.contourArea(c) for c in contour_contours]

    temp = sorted(areas)[-5]
    for i, element in enumerate(areas):
        if element >= temp:
            idx = i
            break

    avg_x = []
    avg_y = []
    for cnt in contour_contours[idx:idx+5]:
        for c in cnt:
            avg_x.append(c[0][0])
            avg_y.append(c[0][1])

    return (np.mean(avg_x), np.mean(avg_y))

    # cv2.circle(contour_i, (int(np.mean(avg_x)), int(
    #     np.mean(avg_y))), 5, (255, 255, 0), -1)
    # cv2.imshow("test_center", contour_i)
    # cv2.imwrite("test_center.jpg", contour_i)
    # cv2.waitKey(0)

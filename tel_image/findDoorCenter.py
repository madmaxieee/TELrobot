import cv2
import numpy as np
# from config import params

color_range = {
    'red0': [[0, 70, 0], [5, 255, 255]],
    'red1': [[175, 70, 0], [180, 255, 255]],
    'yellow': [[25, 70, 0], [30, 255, 255]],
    'green': [[45, 70, 0], [75, 255, 255]],
    'blue': [[100, 70, 0], [125, 255, 255]]
}


def findMask(hsv_img, color):
    if color == 'red':
        lower0, upper0 = np.array(color_range['red0'])
        lower1, upper1 = np.array(color_range['red1'])
        mask0 = cv2.inRange(hsv_img, lower0, upper0)
        mask1 = cv2.inRange(hsv_img, lower1, upper1)
        mask = cv2.bitwise_or(mask0, mask1)
    else:
        lower, upper = np.array(color_range[color])
        mask = cv2.inRange(hsv_img, lower, upper)

    return mask

# TODO return false if no door is found


def findDoorCenter(bgr_img, color) -> tuple:
    kernel = np.ones((1, 1), np.uint8)

    # x_size, y_size = params['cam_size']
    x_size, y_size = (640, 480)
    bgr_img = cv2.resize(bgr_img, (640, 480),
                         interpolation=cv2.INTER_AREA)

    bgr_img = cv2.copyMakeBorder(bgr_img, 5, 5, 5, 5, cv2.BORDER_CONSTANT)

    # blurred = cv2.pyrMeanShiftFiltering(bgr_img, 5, 5)
    blurred = cv2.GaussianBlur(bgr_img, (5, 5), cv2.BORDER_DEFAULT)
    hsv_img = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = findMask(hsv_img, color)
    eroded = cv2.erode(mask, (4, 4), iterations=1)
    dilation = cv2.dilate(eroded, (4, 4), iterations=2)

    # closing = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    # closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    # Getting the edge of morphology
    edge = cv2.Canny(dilation, 125, 175)
    # _, contours,hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    (contour_contours, _) = cv2.findContours(
        edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contour_i = cv2.cvtColor(mask.copy(), cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_i, contour_contours, -1, (0, 0, 255), 2)

    areas = np.array([cv2.contourArea(c) for c in contour_contours])
    # print(areas)

    big_contours = (areas > 500).nonzero()[0]
    # print(big_contours)
    if len(big_contours) == 0:
        return (-1, -1)

    avg_x = []
    avg_y = []

    contour_contours = [contour_contours[i] for i in big_contours]
    cv2.drawContours(contour_i, contour_contours, -1, (255, 0, 0), 2)
    for cnt in contour_contours:
        for c in cnt:
            avg_x.append(c[0][0])
            avg_y.append(c[0][1])

    cv2.circle(contour_i, (int(np.mean(avg_x)), int(
        np.mean(avg_y))), 5, (255, 255, 0), -1)
    cv2.imshow("test_center", contour_i)
    cv2.imwrite("test_center.jpg", contour_i)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

    return (np.mean(avg_x), np.mean(avg_y))


if __name__ == '__main__':
    frame = cv2.imread('./photo2.jpg')
    findDoorCenter(frame, 'green')

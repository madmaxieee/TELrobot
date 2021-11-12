import cv2
import numpy as np

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image[y,x]

        #you might want to adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 20, pixel[1] + 50, pixel[2] + 50])
        lower =  np.array([pixel[0] - 20, pixel[1] - 50, pixel[2] - 50])
        print(pixel, lower, upper)

        image_mask = cv2.inRange(image,lower,upper)
        cv2.imshow("mask",image_mask)

image = cv2.imread("./image1.jpg")
image = cv2.resize(image, (756, 1008), interpolation=cv2.INTER_AREA)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', pick_color)
cv2.imshow("Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()


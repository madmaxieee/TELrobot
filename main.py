import sys
# from controllers.DashBoard import DashBoard
from auto import Auto
from subsystems import base
import cv2 as cv
import numpy as np
from time import sleep

def main():
    if len(sys.argv) == 1:
        pass
        # dash = DashBoard()
        # dash.start()
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'auto':
            base.cartDrive((0, -0.7))
            base.updateMotors()
            sleep(0.1)
            base.clearDriveSpeeds()
            base.updateMotors()

            base.cartDrive((-0.7, 0))
            base.updateMotors()

            # cv.imshow('.', np.zeros((200, 200)))
            # while True:
            #     base.clearDriveSpeeds()
            #     base.updateMotors()
            #     if cv.waitKey(1) & 0xFF == ord(' '):
            #         break
            # print('run')
            # a = Auto()
            # a.start()
            # base.cartDrive((0, -1))
            # base.updateMotors()
            # sleep(0.1)
            # base.clearDriveSpeeds()
            # base.updateMotors()

            # base.cartDrive((1, 0))
            # base.updateMotors()
            # sleep(3)
            # base.clearDriveSpeeds()
            # base.updateMotors()

            # base.cartDrive((0, 1))
            # base.updateMotors()
            # sleep(0.1)
            # base.clearDriveSpeeds()
            # base.updateMotors()

            # base.cartDrive((1, 0))
            # base.updateMotors()
            # sleep(3)
            # base.clearDriveSpeeds()
            # base.updateMotors()

            # base.cartDrive((0, -1))
            # base.updateMotors()
            # sleep(0.1)
            # base.clearDriveSpeeds()
            # base.updateMotors()

            # base.cartDrive((1, 0))
            # base.updateMotors()
            # sleep(3)
            # base.clearDriveSpeeds()
            # base.updateMotors()

        elif sys.argv[1] == 'clean':
            base.clearDriveSpeeds()
            base.updateMotors()
            base.cleanUp()
            exit()
            
        elif sys.argv[1] == 'test':
            # a = Auto()
            # a.test()
            # while True:
            #     pressed_keys = pygame.key.get_pressed()
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT or pressed_keys[pygame.K_SPACE]:
            #             break
            cv.imshow('.', np.zeros((200, 200)))
            while True:
                if cv.waitKey(1) & 0xFF == ord(' '):
                    break
            print('run')


if __name__ == '__main__':
    main()

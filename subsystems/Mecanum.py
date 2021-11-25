from time import sleep

from RPi import GPIO
from Motor import Motor
import numpy as np

# (EN, in2/4, in1/3)
motor_pins = {
    "r_f": (25, 24, 23),
    "l_f": (16, 20, 21),
    "r_b": (11, 9, 10),
    "l_b": (17, 27, 22),
}


def pol2cart(coord):
    r, phi = coord
    phi *= np.pi / 180
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return (x, y)


class Mecanum:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.motor_r_f = Motor(motor_pins["r_f"])
        self.motor_l_f = Motor(motor_pins["l_f"])
        self.motor_r_b = Motor(motor_pins["r_b"])
        self.motor_l_b = Motor(motor_pins["l_b"])

        self.drive_speeds = np.array([0, 0, 0, 0])

    def cartDrive(self, velocity=(0, 0), spin=0):
        # rf, lf, rb, lb
        delta_speeds = np.array([0, 0, 0, 0])
        x_hat = np.array([1, 1, 1, 1])
        y_hat = np.array([1, -1, -1, 1])
        phi_hat = np.array([-1, 1, -1, 1])
        delta_speeds = velocity[0] * x_hat + velocity[1] * \
            y_hat + spin * phi_hat + spin * phi_hat

        self.drive_speeds += delta_speeds

        self.updateMotors()

    def polarDrive(self, coord=(0, 0), spin=0):
        self.cartDrive(pol2cart(coord), spin=0)

    def stop(self):
        self.cartDrive((0, 0))

    def updateMotors(self):
        # normalize speeds
        max_speed = np.max(np.abs(self.drive_speeds))
        if max_speed > 1:
            self.drive_speeds = self.drive_speeds / max_speed

        self.motor_r_f.move(self.drive_speeds[0])
        self.motor_l_f.move(self.drive_speeds[1])
        self.motor_r_b.move(self.drive_speeds[2])
        self.motor_l_b.move(self.drive_speeds[3])

    def clearDriveSpeeds(self):
        self.drive_speeds = np.array([0, 0, 0, 0])

    def test(self):
        self.polarDrive((1, 0))
        sleep(3)
        self.polarDrive((1, -90))
        sleep(2)
        self.polarDrive((1, 0))
        sleep(3)
        # self.polarDrive((1, 45))
        # sleep(3)

    def cleanUp(self):
        GPIO.cleanup()


# to be used in other files
base = Mecanum()

if __name__ == '__main__':
    base.test()
    base.cleanUp()

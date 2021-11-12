from time import sleep

from RPi import GPIO
from Motor import Motor
import numpy as np

# (EN, in2/4, in1/3)
motor_pins = {
    "r_f": (4, 3, 2),
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
        self.motor_r_f = Motor(motor_pins["r_f"])
        self.motor_l_f = Motor(motor_pins["l_f"])
        self.motor_r_b = Motor(motor_pins["r_b"])
        self.motor_l_b = Motor(motor_pins["l_b"])

    def cartDrive(self, velocity, spin=0):
        # rf, lf, rb, lb
        speeds = np.array([0, 0, 0, 0])
        x_hat = np.array([1, 1, 1, 1])
        y_hat = np.array([1, -1, -1, 1])
        phi_hat = np.array([1, -1, 1, -1])
        speeds = velocity[0] * x_hat + velocity[1] * y_hat + spin * phi_hat

        # normalize speeds
        speeds /= np.max(np.abs(speeds))

        self.motor_r_f.move(speeds[0])
        self.motor_l_f.move(speeds[1])
        self.motor_r_b.move(speeds[2])
        self.motor_l_b.move(speeds[3])

    def polarDrive(self, coord, spin=0):
        self.cartDrive(pol2cart(coord), spin=0)

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
    mec = Mecanum()
    mec.test()
    mec.cleanUp()

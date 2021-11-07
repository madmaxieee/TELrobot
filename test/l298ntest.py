import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

class Motor:
    def __init__(self, ena, in1, in2):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        gpio.setup(self.ena, gpio.OUT)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        self.pwm = gpio.PWM(self.ena, 100)
        self.pwm.start(0)

    def moveF(self, dutyCycle=50, sleepTime=0):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)
        self.pwm.ChangeDutyCycle(dutyCycle)
        sleep(sleepTime)

    def moveB(self, dutyCycle=50, sleepTime=0):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)
        self.pwm.ChangeDutyCycle(dutyCycle)
        sleep(sleepTime)

    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)


def init():
    gpio.setmode(gpio.BCM)

def test():
    motor1 = Motor(4, 3, 2)
    while True:
        print('Loop Runnung')

        # if x == 'w':

        motor1.moveF(30, 2)
        motor1.stop(2)
        motor1.moveB(100, 2)
        motor1.stop(2)

print(__name__)
if __name__ == '__main__':
    print('hello')
    test()

import RPi.GPIO as gpio
from time import sleep

class Motor():
    def __init__(self, ena, in1, in2):
        super().__init__()
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        gpio.setup(self.ena, gpio.OUT)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        self.pwm = gpio.PWM(self.ena, 100)
        self.pwm.start(0)
    
    def moveF(self, x = 50, t = 0):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)

    def moveB(self, x = 50, t = 0):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)

    def stop(self, t = 0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)


def init():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

def test():
    motor1 = Motor(25, 24, 23)

    while True:
        x = raw_input()

        print('Loop Runnung')

        # if x == 'w':
            
        motor1.moveF(30, 2)
        motor1.stop(2)
        motor1.moveB(100, 2)
        motor1.stop(2)

if __name__ == 'main':
    init()
    test()

import RPi.GPIO as GPIO
from time import sleep

class Motor:
    def __init__(self, ena, in1, in2):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.ena, 100)
        self.pwm.start(0)

    def moveF(self, dutyCycle=50, sleepTime=0):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(dutyCycle)
        sleep(sleepTime)

    def moveB(self, dutyCycle=50, sleepTime=0):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(dutyCycle)
        sleep(sleepTime)

    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)


def init():
    GPIO.setmode(GPIO.BCM)

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

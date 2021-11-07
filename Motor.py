import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwm_frequency = 100


class Motor:
    def __init__(self, pins: tuple):
        ENA, IN1, IN2 = pins
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        self.PWM = GPIO.PWM(self.ENA, pwm_frequency)
        self.PWM.start(0)

    def move(self, speed=1):
        GPIO.output(self.IN1, 1 if speed > 0 else 0)
        GPIO.output(self.IN2, 0 if speed > 0 else 1)
        # print(f'{abs(speed)}')
        self.PWM.ChangeDutyCycle(abs(speed) * pwm_frequency)

    def stop(self):
        self.PWM.ChangeDutyCycle(0)


if __name__ == '__main__':
    m = Motor((4,3,2))
    m.move()
    time.sleep(5)
    m.stop()
    GPIO.cleanup()

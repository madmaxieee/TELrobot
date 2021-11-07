from time import sleep
import RPi.GPIO as GPIO

ena = 4
in1, in2 = 3, 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
pwm = GPIO.PWM(ena, 100)
pwm.start(0)
pwm.ChangeDutyCycle(100)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
sleep(3)

GPIO.cleanup()

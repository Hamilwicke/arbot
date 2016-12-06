import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servoPin = 4
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)
for i in range(0,180):
    DC = 1/18*(i)+2
    pwm.ChangeDutyCycle(DC)
    time.sleep(.1)
    print i
pwm.stop()
GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servoPin = 4
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)

for i in range(0,20):
    dc = input('pick number 1-20')
    pwm.ChangeDutyCycle(dc)

'''
for i in range(0,180):
    #(0,3)
    DC = 1./18.*(i)+2
    pwm.ChangeDutyCycle(DC)
    time.sleep(.1)
    print i
'''
pwm.stop()
GPIO.cleanup()
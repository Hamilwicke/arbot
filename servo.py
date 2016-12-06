import RPi.GPIO as GPIO
import time
from servosix import ServoSix
ss = ServoSix()

for i in range(0,170):
    ss.set_servo(2, i)
    time.sleep(.05)
    print i
ss.cleanup()



GPIO.setmode(GPIO.BCM)
servoPin = 4
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)


for i in range(0,180):

    DC = 1./20.*(i)+3.1
    pwm.ChangeDutyCycle(DC)
    if i == 1:
        time.sleep(1)
    else:
        time.sleep(.05)
    print i

pwm.stop()
GPIO.cleanup()

'''for i in range(0,20):
    dc = input('pick number 1-20')
    pwm.ChangeDutyCycle(dc)'''

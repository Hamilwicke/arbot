import RPi.GPIO as GPIO
import time
import sensor
snsr = sensor.sensors()
import math


GPIO.setmode(GPIO.BCM)
servoPin = 6
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)



while True:

    for i in range(10, 160, 5):
        DC = 1. / 20. * i + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)

    for i in reversed(range(10, 160, 5)):
        DC = 1./20. * i + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)


pwm.stop()
GPIO.cleanup()
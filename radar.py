import RPi.GPIO as GPIO
import time
import sensor
snsr = sensor.sensors()
import math


GPIO.setmode(GPIO.BCM)
servoPin = 19
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)


while True:

    for i in range(10,160,5):
        DC = 1. / 20. * (i) + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance((snsr.RADAR_TRIG,snsr.RADAR_ECHO))
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)

    for i in reversed(range(10,160,5)):
        DC = 1./20.*(i)+3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance((snsr.RADAR_TRIG, snsr.RADAR_ECHO))
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)


'''
    def collision_reading(theta, hyp):
        if theta > 90:
            angle = 180 - theta
        else:
            angle = theta
        return hyp*math.cos(math.radians(angle))

    def collision_avoidance(self, radar_angle, radar_distance):

        collision_reading = self.collision_reading(radar_angle, radar_distance)
        if radar_angle > 90:
            if collision_reading <= 20:
                return #soft right turn
            if collision_reading <=10:
                return #hard right turn
        if radar_angle < 90:
            if collision_reading <= 20:
                return #soft left turn
            if collision_reading <=10:
                return #hard left turn
'''

pwm.stop()
GPIO.cleanup()
import RPi.GPIO as GPIO
import time
import sensor
import time
import wiringpi
import math

snsr = sensor.sensors()

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.001

while True:
    for pulse in range(60, 230, 5):
        print 'wiringpi.pwmWrite(18, pulse)'
        wiringpi.pwmWrite(18, pulse)
        print 'dist = snsr.average_distance(snsr.radar_sensor)'
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (pulse-60, dist)
        time.sleep(delay_period)
    for pulse in range(230, 60, -5):
        print 'wiringpi.pwmWrite(18, pulse)'
        wiringpi.pwmWrite(18, pulse)
        print 'dist = snsr.average_distance(snsr.radar_sensor)'
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (pulse-60, dist)
        time.sleep(delay_period)

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



pwm.stop()
GPIO.cleanup()


while True:

    for i in range(10, 160, 10):
        DC = 1. / 20. * i + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)

    for i in reversed(range(10, 160, 10)):
        DC = 1./20. * i + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.average_distance(snsr.radar_sensor)
        print 'angle: %s, distance: %s' % (i, dist)
        time.sleep(.05)
'''

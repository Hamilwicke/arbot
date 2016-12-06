import RPi.GPIO as GPIO
import time
import sensor
snsr = sensor.sensors()



GPIO.setmode(GPIO.BCM)
servoPin = 18
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)


while True:

    for i in range(10,170):
        DC = 1. / 20. * (i) + 3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.get_distance((snsr.LEFT_TRIG,snsr.LEFT_ECHO))
        print 'angle: %s, distance: %s' % (i, dist)
    time.sleep(.05)

    for i in reversed(range(0,180)):
        DC = 1./20.*(i)+3
        pwm.ChangeDutyCycle(DC)
        dist = snsr.get_distance((snsr.LEFT_TRIG, snsr.LEFT_ECHO))
        print 'angle: %s, distance: %s' % (i, dist)
    time.sleep(.05)




pwm.stop()
GPIO.cleanup()
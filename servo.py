import RPi.GPIO as GPIO
import time

import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.005

while True:
    for pulse in range(50, 250, 5):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)
    for pulse in range(250, 50, -5):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)


'''
GPIO.setmode(GPIO.BCM)

servoPin = 6
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)


for i in range(0,180):

    DC = 1./20.*i+3
    pwm.ChangeDutyCycle(DC)
    if i == 1:
        time.sleep(1)
    else:
        time.sleep(.01)
    print i



for i in range(0,20):
    dc = input('pick number 1-20')
    DC = 1. / 20. * i + 3
    pwm.ChangeDutyCycle(DC)

pwm.stop()
GPIO.cleanup()
'''
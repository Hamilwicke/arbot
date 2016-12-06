import RPi.GPIO as GPIO

GPIO.setmoade(GPIO.BCM)
servoPin = 4
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)
for i in range(0,20):
    desiredPosition = input("servo position? 0-180: ")
    DC = 1/18.*(desiredPosition)+2
    pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
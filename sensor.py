import RPi.GPIO as GPIO                    # Import GPIO library
import time                                # Import time library

#GPIO.setmode(GPIO.BCM)                     # Set GPIO pin numbering


class sensors():
    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        # Assign all pins
        self.LEFT_TRIG = 16
        self.LEFT_ECHO = 19
        self.RIGHT_TRIG = 20
        self.RIGHT_ECHO = 21
        self.RADAR_TRIG = 13
        self.RADAR_ECHO = 12
        self.servoPin = 18

        #4grey,17purp,6blue,27green,22yell,23oran,24red,25brown,5black,
        #5vblue,3vyell,GNDgreen

        # Setup pins for input or output
        GPIO.setup(self.LEFT_TRIG, GPIO.OUT)
        GPIO.setup(self.LEFT_ECHO, GPIO.IN)
        GPIO.setup(self.RIGHT_TRIG, GPIO.OUT)
        GPIO.setup(self.RIGHT_ECHO, GPIO.IN)
        GPIO.setup(self.RADAR_TRIG, GPIO.OUT)
        GPIO.setup(self.RADAR_ECHO, GPIO.IN)
        GPIO.setup(self.servoPin, GPIO.OUT)

        # Build sensor objects
        self.right_sensor = [self.RIGHT_TRIG, self.RIGHT_ECHO]
        self.left_sensor = [self.LEFT_TRIG, self.LEFT_ECHO]
        self.radar_sensor = [self.RADAR_TRIG, self.RADAR_ECHO]

        # Setup the servo for radar
        self.pwm = GPIO.PWM(self.servoPin, 50)

    def get_distance(self, (TRIG, ECHO)):

        pulse_start = time.time()
        pulse_end = time.time()
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            if pulse_end - pulse_start > 0.0174:
                #time.sleep(.001)
                return 200

        distance = ((pulse_end - pulse_start) * 34300) / 2

        time.sleep(.001)
        return distance

    def average_distance(self, sensor):
        sampled_distance = lambda n: sum([self.get_distance(sensor) for n in range(n)]) / float(n)
        distance = sampled_distance(15)
        return distance

    def forward_left(self):
        left = self.get_distance(self.left_sensor)
        return left

    def forward_right(self):
        right = self.get_distance(self.right_sensor)
        return right

    def radar(self):
        self.pwm.start(7)

        while True:

            for angle in range(10, 160, 5):
                DC = 1. / 20. * (angle) + 3
                self.pwm.ChangeDutyCycle(DC)
                dist = self.average_distance(self.radar_sensor)
                return dist, angle


            for angle in reversed(range(10, 160, 5)):
                DC = 1. / 20. * (angle) + 3
                self.pwm.ChangeDutyCycle(DC)
                dist = self.average_distance(self.radar_sensor)
                return dist, angle


    def all_sensors(self):

        pwm.start(7)
        while True:

            for angle in range(10, 160, 5):
                DC = 1. / 20. * angle + 3
                self.pwm.ChangeDutyCycle(DC)
                radar_distance = self.average_distance(self.radar_sensor)
                forward_left = self.average_distance(self.left_sensor)
                forward_right = self.average_distance(self.right_sensor)
                return forward_left, forward_right, radar_distance, angle

            for angle in reversed(range(10, 160, 5)):
                DC = 1. / 20. * (angle) + 3
                self.pwm.ChangeDutyCycle(DC)
                radar_distance = self.average_distance(self.radar_sensor)
                forward_left = self.average_distance(self.left_sensor)
                forward_right = self.average_distance(self.right_sensor)
                return forward_left, forward_right, radar_distance, angle











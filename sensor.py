import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import random
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

class sensors():
  def __init__(self):
    self.LEFT_TRIG = 5
    self.LEFT_ECHO = 12
    self.RIGHT_TRIG = 17
    self.RIGHT_ECHO = 23
    self.RADAR_TRIG = 20
    self.RADAR_ECHO = 21

    GPIO.setup(self.LEFT_TRIG, GPIO.OUT)
    GPIO.setup(self.LEFT_ECHO, GPIO.IN)
    GPIO.setup(self.RIGHT_TRIG, GPIO.OUT)
    GPIO.setup(self.RIGHT_ECHO, GPIO.IN)
    GPIO.setup(self.RADAR_TRIG, GPIO.OUT)
    GPIO.setup(self.RADAR_ECHO, GPIO.IN)

    self.right_sensor = [self.RIGHT_TRIG, self.RIGHT_ECHO]
    self.left_sensor = [self.LEFT_TRIG, self.LEFT_ECHO]



  def get_distance(self, (TRIG, ECHO)):
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(round(random.uniform(.05, .03), 3))
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)                 #Set TRIG as LOW


    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse
    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse

    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    #print 'pulse start time =%s' % (pulse_start)
    #print 'pulse end time =%s' % (pulse_end)
    #print 'pulse duration = %s'%(pulse_duration)
    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    #print 'distance = %s'%(distance)
    #if distance > 6 and distance < 200:      #Check whether the distance is within range
    GPIO.cleanup(TRIG)
    GPIO.cleanup(ECHO)

    return distance - 0.5

  def forward_left(self):
    left = self.get_distance(self.left_sensor)
    return left

  def forward_right(self):
    right = self.get_distance(self.right_sensor)
    return right


  def pulse(self, TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
      pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
      pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)
    if distance > 2 and distance < 400:  # Check whether the distance is within range
      return distance - 0.5
    else:
      return None














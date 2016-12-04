import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

class sensors():
  def __init__(self):
    self.LEFT_TRIG = 20
    self.LEFT_ECHO = 21
    self.RIGHT_TRIG = 16
    self.RIGHT_ECHO = 19

    GPIO.setup(self.LEFT_TRIG, GPIO.OUT)
    GPIO.setup(self.LEFT_ECHO, GPIO.IN)
    GPIO.setup(self.RIGHT_TRIG, GPIO.OUT)
    GPIO.setup(self.RIGHT_ECHO, GPIO.IN)

    self.right_sensor = [self.RIGHT_TRIG, self.RIGHT_ECHO]
    self.left_sensor = [self.LEFT_TRIG, self.LEFT_ECHO]



  def get_distance(self, (TRIG, ECHO)):

    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    print 'triggering pulse'
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW


    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse
    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse


    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    print 'pulse start time =%s' % (pulse_start)
    print 'pulse end time =%s' % (pulse_end)
    print 'pulse duration = %s'%(pulse_duration)
    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    print 'distance = %s'%(distance)
    if distance > 2 and distance < 400:      #Check whether the distance is within range
      return distance - 0.5
    else:
      return None


  def forward_distance(self):
    print 'getting LEFT sensor distance'
    self.left = self.get_distance(self.left_sensor)
    time.sleep(.05)
    print 'getting RIGHT sensor distance'
    self.right = self.get_distance(self.right_sensor)
    time.sleep(.05)
    return self.left, self.right


  def get_multi_sensor_distance(self):
    Master_Trig = self.LEFT_TRIG
    Master_Echo = self.LEFT_ECHO
    Slave_Trig = self.RIGHT_TRIG
    Slave_Echo = self.RIGHT_ECHO

    self.pulse(Master_Trig)
    print 'master pulse sent'
    master_distance = self.listen(Master_Echo)
    while GPIO.input(Slave_Echo) == 1:  # Check whether the ECHO is HIGH
      #pulse_end = time.time()


    #while time.time() - pulse_end >= .05:
      time.sleep(.05)
      self.pulse(Slave_Trig)
      slave_distance = self.listen(Slave_Echo)

      return master_distance, slave_distance


  def listen(self,ECHO):
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

  def pulse(self, TRIG):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)














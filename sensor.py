import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

LEFT_TRIG = 20                                  #Associate pin 23 to TRIG
LEFT_ECHO = 21                                  #Associate pin 24 to ECHO
RIGHT_TRIG = 16
RIGHT_ECHO = 19

print "Distance measurement in progress"

GPIO.setup(LEFT_TRIG, GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(LEFT_ECHO, GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(LEFT_TRIG, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(LEFT_TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(LEFT_TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(LEFT_ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(LEFT_ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
  else:
    print "Out Of Range"                   #display out of range
import sensor
import time

sn = sensor.sensors()

while True:
    print sn.forward_distance()
    time.sleep(.05)
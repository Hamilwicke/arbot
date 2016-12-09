import sensor
import time


sn = sensor.sensors()

while True:
    print sn.radar()


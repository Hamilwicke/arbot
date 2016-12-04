import sensor
import time

sn = sensor.sensors()

while True:
    print '============='
    print sn.forward_distance()
    print '============='
    time.sleep(5)
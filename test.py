import sensor
import time

sn = sensor.sensors()

while True:
    print '============='
    print sn.get_multi_sensor_distance()
    print '============='
    time.sleep(5)
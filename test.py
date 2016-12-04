import sensor
import time

sn = sensor.sensors()

while True:
    # print '============='
    print sn.forward_distance()
    #print sn.get_multi_sensor_distance()
    # print '============='
    time.sleep(.1)


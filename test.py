import sensor
import time


sn = sensor.sensors()

while True:
    print '============='
    print 'left = %s,  other %s' % (sn.forward_left(), sn.other_sensor())
    #print sn.get_multi_sensor_distance()
    #print sn.get_multi_sensor_distance()
    print '============='
    time.sleep(1)


import sensor
import time


sn = sensor.sensors()

while True:
    #print '============='
    print 'left = %s, right = %s, other = %s' % (sn.forward_left(),sn.forward_right(), sn.other_sensor())
    #print sn.get_multi_sensor_distance()
    #print sn.get_multi_sensor_distance()
    #print '============='
    time.sleep(.1)


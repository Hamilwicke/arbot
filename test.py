import sensor
import time


sn = sensor.sensors()

while True:
    #print '============='
    print 'left = , right = %s, other = ' % (sn.average_distance(sn.right_sensor))
    #print sn.get_multi_sensor_distance()
    #print sn.get_multi_sensor_distance()
    #print '============='
    time.sleep(.05)


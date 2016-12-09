import sensor
import time


sn = sensor.sensors()

while True:
    #print '============='
    print 'left = %s, right = %s, radar = %s' % (sn.average_distance(sn.left_sensor),
                                                 sn.average_distance(sn.right_sensor),
                                                 sn.average_distance(sn.radar_sensor))
    #print sn.get_multi_sensor_distance()
    #print sn.get_multi_sensor_distance()
    #print '============='
    #time.sleep(.)


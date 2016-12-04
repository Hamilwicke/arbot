import sensor

sn = sensor.sensors()

while True:
    print sn.get_multi_sensor_distance()
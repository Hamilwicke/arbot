import sensor

sn = sensor.sensors()

while True:
    print sn.forward_distance()
import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]

while True:
    if snsr.forward_distance() >= 10:
        arbot.forward(125)

    else:
        arbot.right_turn(1)

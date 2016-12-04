import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]

while True:
    if snsr.forward_distance()[0] >= 10 and snsr.forward_distance()[1] >= 10:
        arbot.forward(125)

    else:
        arbot.right_turn(1)

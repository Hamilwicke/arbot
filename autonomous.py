import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]

while True:
    arbot.forward(115)
    if snsr.forward_distance()[0] <= 10:
        arbot.right_turn(155,1)
        pass
    if snsr.forward_distance()[1] <= 10:
        arbot.left_turn(155,1)
        pass


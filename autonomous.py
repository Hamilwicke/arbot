import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]

while True:
    try:
        print 'Forward'
        arbot.forward(155)
        arbot.forward(115)

        if snsr.forward_distance()[0] <= 10 or snsr.forward_distance()[0] == None:
            print 'left sensor proximity warning: making right turn'
            arbot.right_turn(155,1)
            pass
        if snsr.forward_distance()[1] <= 10 or snsr.forward_distance()[1] == None:
            print 'right sensor proximity warning: making left turn'
            arbot.left_turn(155,1)
            pass
    except KeyboardInterrupt:
        print 'keyboard interrupt received'
        arbot.turnOffMotors()


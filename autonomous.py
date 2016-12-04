import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]
crusing_speed = 115
while True:
    try:
        print 'Forward'
        arbot.forward(155)
        arbot.forward(crusing_speed)

        if snsr.forward_distance()[0] <= 10 or snsr.forward_distance()[0] == None:
            print 'left sensor proximity warning: making right turn'
            arbot.stop(crusing_speed)
            arbot.right_turn(255,1)
            pass
        if snsr.forward_distance()[1] <= 10 or snsr.forward_distance()[1] == None:
            print 'right sensor proximity warning: making left turn'
            arbot.stop(crusing_speed)
            arbot.left_turn(255,1)
            pass
    except KeyboardInterrupt:
        print 'keyboard interrupt received'
        arbot.turnOffMotors()


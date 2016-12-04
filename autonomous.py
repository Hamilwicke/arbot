import driving
import sensor

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]
crusing_speed = 115
stopping_distance = 25

while True:
    left_sensor = snsr.forward_distance()[0]
    right_sensor = snsr.forward_distance()[1]
    print left_sensor, right_sensor
    try:

        arbot.forward(155)
        arbot.forward(crusing_speed)

        if left_sensor <= stopping_distance:
            print 'left sensor proximity warning: making right turn'
            arbot.stop(crusing_speed)
            arbot.right_turn(255,1)
            print 'forward'
            pass
        if right_sensor <= stopping_distance:
            print 'right sensor proximity warning: making left turn'
            arbot.stop(crusing_speed)
            arbot.left_turn(255,1)
            print 'forward'
            pass
    except KeyboardInterrupt:
        print 'keyboard interrupt received'
        arbot.turnOffMotors()


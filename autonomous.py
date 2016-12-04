import driving
import sensor
import time

arbot = driving.motion()
snsr = sensor.sensors()
left_sensor = snsr.forward_distance()[0]
right_sensor = snsr.forward_distance()[1]
crusing_speed = 255
stopping_distance = 25

while True:

    try:
        left_sensor = snsr.forward_distance()[0]
        right_sensor = snsr.forward_distance()[1]
        print left_sensor, right_sensor
        arbot.forward(155)
        arbot.forward(crusing_speed)

        if left_sensor <= stopping_distance:
            print 'left sensor proximity warning: making right turn'
            arbot.stop(crusing_speed)
            time.sleep(.5)
            arbot.right_turn(255,.5)
            print 'forward'
            time.sleep(.5)
            pass
        if right_sensor <= stopping_distance:
            print 'right sensor proximity warning: making left turn'
            arbot.stop(crusing_speed)
            time.sleep(.5)
            arbot.left_turn(255,.5)
            print 'forward'
            time.sleep(.5)
            pass

    except KeyboardInterrupt:
        print 'keyboard interrupt received'
        arbot.turnOffMotors()


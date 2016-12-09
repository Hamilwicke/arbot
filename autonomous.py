import driving
import sensor
import time
import threading
from threading import Thread

arbot = driving.motion()
snsr = sensor.sensors()
crusing_speed = 135
stopping_distance = 25

Thread(target=snsr.forward_left()).start()
Thread(target=snsr.forward_right).start()
Thread(target=snsr.radar).start()


while True:

    try:
        left_sensor = snsr.forward_left()
        right_sensor = snsr.forward_right()


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


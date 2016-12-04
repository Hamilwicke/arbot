

import driving
import time
speed = 155
robot = driving.motion()

while True:
        try:
                robot.forward(155)
                time.sleep(2)
                robot.backward(155)
                time.sleep(2)
                robot.right_turn(155)
                time.sleep(1)
                robot.forward(155)
                time.sleep(2)
                robot.left_turn(155)
                time.sleep(1)
                robot.backward(155)
        except KeyboardInterrupt:
                robot.turnOffMotors()
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit


class motion():
    def __init__(self):
        self.mh = Adafruit_MotorHAT(addr=0x60)
        self.rightFront = self.mh.getMotor(1)
        self.rightRear = self.mh.getMotor(3)
        self.leftFront = self.mh.getMotor(2)
        self.leftRear = self.mh.getMotor(4)

    def turnOffMotors(self):
        '''
        Will shut down motor upon pressing ctrl + c
        '''
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def smooth_accelerate(self, speed, wheel):
        for i in range(speed):
            wheel.setSpeed(i)
            time.sleep(0.001)
            return i

    def smooth_decelerate(self, speed, wheel):
        for i in reversed(range(speed)):
            wheel.setSpeed(i)
            time.sleep(0.001)
            return i

    def forward(self, speed, seconds=None):
        '''
        Moves robot forward at designated speed
        '''

        self.rightFront.setSpeed(speed)
        self.rightRear.setSpeed(speed)
        self.leftFront.setSpeed(speed)
        self.leftRear.setSpeed(speed)
        self.rightFront.run(Adafruit_MotorHAT.FORWARD)
        self.rightRear.run(Adafruit_MotorHAT.FORWARD)
        self.leftFront.run(Adafruit_MotorHAT.FORWARD)
        self.leftRear.run(Adafruit_MotorHAT.FORWARD)
        if seconds is not None:
            time.sleep(seconds)
            self.stop(speed)

    def backward(self, speed, seconds=None):
        '''
        Moves robot forward at designated speed
        '''

        self.rightFront.setSpeed(speed)
        self.rightRear.setSpeed(speed)
        self.leftFront.setSpeed(speed)
        self.leftRear.setSpeed(speed)
        self.rightFront.run(Adafruit_MotorHAT.BACKWARD)
        self.rightRear.run(Adafruit_MotorHAT.BACKWARD)
        self.leftFront.run(Adafruit_MotorHAT.BACKWARD)
        self.leftRear.run(Adafruit_MotorHAT.BACKWARD)
        if seconds is not None:
            time.sleep(seconds)
            self.stop(speed)

    def current_speed(self):
        #don't yet know how to find current speed
        current_speed = None
        return current_speed

    def stop(self, speed, seconds=None):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        '''for i in reversed(range(speed)):
            self.rightFront.setSpeed(i)
            time.sleep(0.001)
        self.rightFront.run(Adafruit_MotorHAT.RELEASE)
        for i in reversed(range(speed)):
            self.rightRear.setSpeed(i)
            time.sleep(0.001)
        self.rightRear.run(Adafruit_MotorHAT.RELEASE)
        for i in reversed(range(speed)):
            self.leftFront.setSpeed(i)
            time.sleep(0.001)
        self.rightFront.run(Adafruit_MotorHAT.RELEASE)
        for i in reversed(range(speed)):
            self.leftRear.setSpeed(i)
            time.sleep(0.001)
        self.leftRear.run(Adafruit_MotorHAT.RELEASE)'''


    def right_turn(self, speed, seconds=None):
        self.leftFront.setSpeed(speed)
        self.leftFront.run(Adafruit_MotorHAT.FORWARD)
        self.leftRear.setSpeed(speed)
        self.leftRear.run(Adafruit_MotorHAT.FORWARD)
        self.rightFront.setSpeed(speed)
        self.rightFront.run(Adafruit_MotorHAT.BACKWARD)
        self.rightRear.setSpeed(speed)
        self.rightRear.run(Adafruit_MotorHAT.BACKWARD)
        if seconds is not None:
            time.sleep(seconds)
            self.stop(speed)

    def left_turn(self, speed, seconds=None):
        self.leftFront.setSpeed(speed)
        self.leftFront.run(Adafruit_MotorHAT.BACKWARD)
        self.leftRear.setSpeed(speed)
        self.leftRear.run(Adafruit_MotorHAT.BACKWARD)
        self.rightFront.setSpeed(speed)
        self.rightFront.run(Adafruit_MotorHAT.FORWARD)
        self.rightRear.setSpeed(speed)
        self.rightRear.run(Adafruit_MotorHAT.FORWARD)
        if seconds is not None:
            time.sleep(seconds)
            self.stop(speed)



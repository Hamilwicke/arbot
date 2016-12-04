import serial
import driving
speed = 155
js = serial.Serial('/dev/cu.usbmodem621', 9600)
print(js.name)

def joystick_output():
    if (js.inWaiting() > 0):
        myData = js.readline().rsplit()
        x, y, click = myData[1], myData[3], myData[5]
        print (x,y,click)
        if x == 0:
            driving.motion.forward(speed=speed)
        if x == 1023:
            driving.motion.backward(speed=speed)
        if y == 0 and x < 1023 and x > 0:
            driving.motion.right_turn(speed=speed)
        if y == 1023 and x < 1023 and x > 0:
            driving.motion.left_turn(speed=speed)

while (1==1):
    try:
        joystick_output()
    except KeyboardInterrupt:
        js.close()



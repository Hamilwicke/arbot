import serial

ser = serial.Serial('/dev/cu.usbmodem621', 9600)
print(ser.name)

while (1==1):
    if (ser.inWaiting()>0):
        myData = ser.readline()
        print myData

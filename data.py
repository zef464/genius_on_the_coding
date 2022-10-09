import time
import serial # noqa
import datetime

ser = serial.Serial(port='COM5', baudrate=9600)
received = []

ser.write(b'begin\n')
time.sleep(5)

while ser.inWaiting() > 0:
    line = ser.readline()
    if line:
        received.append(line.decode().strip())
        now_time = (str(datetime.now().time()))[:8] + ':' # noqa
        print(now_time + received) # noqa

import serial
import time

esp = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

while True:
    # esp.write(bytes(x, 'utf-8'))
    print(esp.readline())

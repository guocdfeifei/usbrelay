import serial
import time

fd = serial.Serial("COM2", 9600)
time.sleep(1)
fd.write('x50')
time.sleep(0.5)
fd.write('x51')


def relay_1():
    fd.write('x00')
    time.sleep(1)


fd.write('x01')

if __name__ == "__main__":
    relay_1()
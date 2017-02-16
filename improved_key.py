import sys,tty
import serial

def encode_command(motor, steps):
    if(motor == 1):
        initial_byte=0b00010000
    elif(motor == 2):
        initial_byte=0b00100000
    else:
        initial_byte=0b00110000
    if(steps < 0):
        initial_byte |= 1 << 7
        steps = abs(steps)
    for i in range(0,4):
        print bin(-steps)
        initial_byte ^= (-((steps >> i) & 1) ^ initial_byte) & (1 << i)
    print bin(initial_byte)


if __name__ == "__main__":
    encode_command(3,-5)

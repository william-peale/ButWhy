import sys,tty,termios
import serial
ser = serial.Serial('/dev/tty.usbmodem1421',9600)
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

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
        
def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
                ser.write(encode_command(1,5))
        elif k=='\x1b[B':
                print "down"
                ser.write(encode_command(1,5))
        elif k=='\x1b[C':
                print "right"
                ser.write(encode_command(1,5))
        elif k=='\x1b[D':
                print "left"
                ser.write(encode_command(1,5))
        elif k =='aaa':
                print "a"
                ser.write(encode_command(1,5))
        elif k =='bbb':
                print "b"
                ser.write(encode_command(1,5))
        elif k =='zzz':
                exit(0)    
        else:
                print "not an arrow key! {}".format(k)

#Seriously wtf
def main():
        while True:
            get()

if __name__=='__main__':
        main()

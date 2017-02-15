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

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
                ser.write("000020000010".encode())
        elif k=='\x1b[B':
                print "down"
                ser.write("000020000000".encode())
        elif k=='\x1b[C':
                print "right"
                ser.write("010000000100".encode())
        elif k=='\x1b[D':
                print "left"
                ser.write("010000000000".encode())
        elif k =='aaa':
                print "a"
                ser.write("000000020000".encode())
        elif k =='bbb':
                print "b"
                ser.write("000000020001".encode())
        else:
                print "not an arrow key! {}".format(k)

def main():
        for i in range(0,1000):
                get()

if __name__=='__main__':
        main()
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

def func(a,b):
    return a+b

def blinkIt():

    board.digital[8].write(1)
    time.sleep(1)
    board.digital[8].write(0)
    
def lightOn():

    board.digital[8].write(1)


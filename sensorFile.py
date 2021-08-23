import math
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()
analog_input = board.get_pin('a:0:i')

def SenseIt():

    analog_value = analog_input.read()
    return(analog_value)


def moreMATH(a, b):
    return math.sqrt((a*a)+(b*b))
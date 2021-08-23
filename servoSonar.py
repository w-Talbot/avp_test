import time
import pyfirmata
import sensorFile

board = pyfirmata.Arduino('/dev/ttyACM0')

def setup():
    #set to know first position: 90

def servoSweep():
    i = 1
    while i < 180:
        #loop through 0-180 by some degrees

        #call the sensor/sonar file to check distance
        val = sensorFile.SenseIt()

        if val > 0: #if something is there record it
            #store values ( val AND i )  in a JSON file (should this be here or in another file?)


        i+=1

#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import time
import pygame
import RPi.GPIO as GPIO
import sensorFile
import functionBlink


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set which GPIO pins the drive outputs are connected to
DRIVE_FORWARD = 18 #
DRIVE_BACKWARD = 23  #
DRIVE_LEFT = 14 #
DRIVE_RIGHT = 4 #


# Set all of the drive pins as output pins
GPIO.setup(DRIVE_FORWARD, GPIO.OUT)
GPIO.setup(DRIVE_BACKWARD, GPIO.OUT)
GPIO.setup(DRIVE_LEFT, GPIO.OUT)
GPIO.setup(DRIVE_RIGHT, GPIO.OUT)

# Function to set all drives off
def MotorOff():
    GPIO.output(DRIVE_FORWARD, GPIO.LOW)
    GPIO.output(DRIVE_BACKWARD, GPIO.LOW)
    GPIO.output(DRIVE_LEFT, GPIO.LOW)
    GPIO.output(DRIVE_RIGHT, GPIO.LOW)

# Settings for JoyBorg
leftDrive = DRIVE_FORWARD                     # Drive number for left motor
rightDrive = DRIVE_BACKWARD                    # Drive number for right motor
forwardDrive = DRIVE_LEFT                  #Drive number for Forward motor
backwardDrive = DRIVE_RIGHT                     #Drive number for Reverse motor
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = True              # Set this to True if up and down appear to be swapped
axisLeftRight = 3                       # Joystick axis to read for left / right position
axisLeftRightInverted = True           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

# Setup pygame and key states
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit

global squareEvent
global circleEvent
global triangleEvent
global xcrossEvent

squareEvent = False
circleEvent = False
triangleEvent = False
xcrossEvent = False

hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("JoyBorg - Press [ESC] to quit")

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    global moveQuit
    global squareEvent
    global circleEvent
    global triangleEvent
    global xcrossEvent
    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = True
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = False
        elif event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            xcross = joystick.get_button(0)
            circle = joystick.get_button(1)
            triangle = joystick.get_button(2)
            square = joystick.get_button(3)
            
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            # Determine Up / Down values
            if upDown < -0.1:
                moveUp = True
                moveDown = False
            elif upDown > 0.1:
                moveUp = False
                moveDown = True
            else:
                moveUp = False
                moveDown = False
            # Determine Left / Right values
            if leftRight < -0.1:
                moveLeft = True
                moveRight = False
            elif leftRight > 0.1:
                moveLeft = False
                moveRight = True
            else:
                moveLeft = False
                moveRight = False
            # Determine SYMBOL values
            if triangle == True:
                triangleEvent = True
            elif square == True:
                squareEvent = True
            elif xcross == True:
                xcrossEvent = True
            elif circle == True:
                circleEvent = True
            else:
                xcrossEvent = False
                circleEvent = False
                triangleEvent = False
                squareEvent = False
                
                
                
                
try:
   # print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent:
            # Keys have changed, generate the command list based on keys
     
            hadEvent = False
            
            if moveQuit:
                break
            elif moveLeft:
                leftState = GPIO.HIGH
                rightState = GPIO.LOW
            elif moveRight:
                leftState = GPIO.LOW
                rightState = GPIO.HIGH
            elif moveUp:
                upState = GPIO.HIGH
                downState = GPIO.LOW
            elif moveDown:
                upState = GPIO.LOW
                downState = GPIO.HIGH
            elif xcrossEvent:
                print("xcross")
            elif circleEvent:
                print("circle")
            elif triangleEvent:
                print("triangle")
            elif squareEvent:
                functionBlink.lightOn()
                print("square")
            else:
                leftState = GPIO.LOW
                rightState = GPIO.LOW
                upState = GPIO.LOW
                downState = GPIO.LOW

                
            GPIO.output(leftDrive, leftState)
            GPIO.output(rightDrive, rightState)
            GPIO.output(forwardDrive, upState)
            GPIO.output(backwardDrive, downState)
        # Wait for the interval period
        time.sleep(interval)
    # Disable all drives
    MotorOff()
except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    MotorOff()

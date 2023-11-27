import RPi.GPIO as GPIO
import time


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37,GPIO.OUT) #PWMR
    GPIO.setup(38,GPIO.OUT) #PWML
    GPIO.setup(32,GPIO.OUT) #L_EN
    GPIO.setup(33,GPIO.OUT) #R_EN
    GPIO.output(37, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)

def move_joystick(input_message):

#Forward
#condtion: right trigger

#sideways
#condition: joystick off center in x direction

#Reverse
#condition:left trigger 

#standstill
#condition: left and right trigger down at all 

def move_arrow(input_message):
    #Forward
    #condtion: arrow key up

    #sideways
    #condition: arrow key left or right 

    #Reverse
    #condition arrow key down 

    #standstill
    #condition: arrow keys up and down 






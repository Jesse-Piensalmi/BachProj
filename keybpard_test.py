from pynput import keyboard
import Jetson.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT) #PWM
GPIO.setup(32,GPIO.OUT) #PWM
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
global dcr
global dcl
dcr=0
dcl=0
pwml = GPIO.PWM(33, 100)
pwmr = GPIO.PWM(32, 100)
GPIO.output(35, GPIO.HIGH)
GPIO.output(37, GPIO.HIGH)

# Function to set the PWM duty cycle and print the new duty cycle


# Function to handle keypress events
def on_key_press(key):
    global dcr  # Declare dcr as global to modify it
    global dcl
    try:
        print(key.char)
        if key.char == 'd':
            print("Right arrow pressed")
            if dcr<100:
                dcr+=1
                if dcl>0:
                    dcl-=1
            
        elif key.char == 'a':
            print("left arrow pressed")
            if dcl<100:
                dcl +=1
                if dcr>0:
                    dcr-=1
        elif key.char =='q':
            print("Q pressed - exiting program")
            raise KeyboardInterrupt
        pwmr.ChangeDutyCycle(dcr)
        pwml.ChangeDutyCycle(dcl)
        print(f"New duty cycle: {dcl}")
    except AttributeError:
        pass  # Ignore non-character keysad

# Set up a listener for key presses
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

# Initial duty cycle


try:
    while True:
        # Your PWM control loop can run here
        pass
except KeyboardInterrupt:
    pass

# Clean up GPIO and stop the listener
listener.stop()
pwml.stop()
pwmr.stop()
GPIO.cleanup()

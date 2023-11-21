from pynput import keyboard
import Jetson.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT) #L_EN
GPIO.setup(22,GPIO.OUT) #R_EN
GPIO.setup(32,GPIO.OUT) #PWMR
GPIO.setup(33,GPIO.OUT) #PWMR


GPIO.output(21, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

# Function to set the PWM duty cycle and print the new duty cycle


# Function to handle keypress events
def on_key_press(key):
    
    try:
        print(key.char)
        if key.char == 'w':
            print("Right arrow pressed")
            GPIO.output(32, GPIO.HIGH)
            GPIO.output(33, GPIO.LOW)
            
        elif key.char == 's':
            print("left arrow pressed")
            GPIO.output(32, GPIO.LOW)
            GPIO.output(33, GPIO.HIGH)
        elif key.char =='q':
            listener.stop()
            GPIO.output(32, GPIO.LOW)
            GPIO.output(33, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.cleanup()
            GPIO.cleanup()
            print("Q pressed - exiting program")
            raise KeyboardInterrupt
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
GPIO.output(32, GPIO.LOW)
GPIO.output(33, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.cleanup()
GPIO.cleanup()

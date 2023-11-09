import Jetson.GPIO as GPIO
import time
import keyboard


GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

pwml = GPIO.PWM(33,100)
pwmr = GPIO.PWM(32,100)

dcl=0
dcr=0
pwml.start(dcl)
pwmr.start(dcr)

def on_key_event(e):
    global dcr
    global dcl
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'right':
            print("Right arrow pressed")
            if dcr<100:
                dcr+=1
                if dcl>0:
                    dcl-=1
            
        elif e.name == 'left':
            print("left arrow pressed")
            if dcl<100:
                dcl +=1
                if dcr>0:
                    dcr-=1
        elif e.name =='q':
            print("Q pressed - exiting program")
            raise KeyboardInterrupt
        pwmr.ChangeDutyCycle(dcr)
        pwml.ChangeDutyCycle(dcl)

keyboard.hook(on_key_event)
try:
    while True:
        print(f"current duty cycle: {dcl}")
except KeyboardInterrupt:
    pass

keyboard.unhook_all()
pwml.stop()
pwmr.stop()
GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)

try:
    while True:
        GPIO.output(32,GPIO.HIGH)
        time.sleep(3)

        GPIO.output(32,GPIO.LOW)
        time.sleep(3)

except KeyboardInterrupt:
    
    GPIO.cleanup()    
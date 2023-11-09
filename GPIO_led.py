import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led_pin = 12

GPIO.setup(led_pin,GPIO.OUT)


try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)

        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:
    pass
GPIO.cleanup()




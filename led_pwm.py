import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32 ,GPIO.OUT)
pwm_en=GPIO.PWM(32,100)
pwm_en.start(50)

try:
    while True:
        for i in range(100):
            pwm_en.ChangeDutyCycle(i)
            time.sleep(1)

except KeyboardInterrupt:
    pwm_en.ChangeDutyCycle(0)
    GPIO.cleanup()
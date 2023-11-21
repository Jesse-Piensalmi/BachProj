import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT) #PWMR
GPIO.setup(22,GPIO.OUT) #PWML
GPIO.setup(32,GPIO.OUT) #L_EN
GPIO.setup(33,GPIO.OUT) #R_EN
GPIO.output(21, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)
#use PWM on the L_EN and R_EN at the same time to modulate the signals going through
#use normal GPIO on LPWM and RPWM
#lpwm=GPIO.PWM(32, 255)
#rpwm=GPIO.PWM(33, 255)
#lpwm.start(0)
#rpwm.start(0)
try:
    while True:
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(33, GPIO.HIGH)
        time.sleep(3)

        GPIO.output(32, GPIO.LOW)
        GPIO.output(33, GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
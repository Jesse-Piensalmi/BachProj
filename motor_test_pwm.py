import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT) #PWMR
GPIO.setup(38,GPIO.OUT) #PWML
GPIO.setup(32,GPIO.OUT) #L_EN
GPIO.setup(33,GPIO.OUT) #R_EN
GPIO.output(37, GPIO.HIGH)
GPIO.output(38, GPIO.LOW)
#use PWM on the L_EN and R_EN at the same time to modulate the signals going through
#use normal GPIO on LPWM and RPWM
lpwm=GPIO.PWM(32, 255)
lpwm.start(100)


try:
    while True:
        for i in range(100):
            lpwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()
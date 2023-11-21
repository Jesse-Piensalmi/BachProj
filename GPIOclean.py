import Jetson.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT) #L_EN
GPIO.setup(22,GPIO.OUT) #R_EN
GPIO.setup(32,GPIO.OUT) #PWMR
GPIO.setup(33,GPIO.OUT) #PWMR
GPIO.output(32, GPIO.LOW)
GPIO.output(33, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.cleanup()
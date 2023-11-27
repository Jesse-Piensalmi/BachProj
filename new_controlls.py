import asyncio
import websockets
import get_ip_address
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT) #PWMR
GPIO.setup(38,GPIO.OUT) #PWML
GPIO.setup(32,GPIO.OUT) #L_EN
GPIO.setup(33,GPIO.OUT) #R_EN
GPIO.output(37, GPIO.LOW)
GPIO.output(38, GPIO.LOW)
lpwm=GPIO.PWM(32,255)
rpwm=GPIO.PWM(33,255)
lpwm.start(0)
rpwm.start(0)
left_joystick_x=0.0
right_trigger=0.0
left_trigger=0.0
cur_duty=0 

async def handle_websockets(websocket,path):
    global left_joystick_x
    global right_trigger
    global left_trigger
    global cur_duty

    async for message in websocket:
        
        if message == ' ':
            print("Yeah")
        else:
            print(f"Received: {message}")
            msg_type, value=message.split()
            print(msg_type, value)
            if msg_type == 'JX':
                #joystick values
                left_joystick_x=float(value)
                left_pwm=int(100*(1-left_joystick_x))
                right_pwm=int(100*(1+left_joystick_x))
                lpwm.ChangeDutyCycle(left_pwm*cur_duty)
                rpwm.ChangeDutyCycle(right_pwm*cur_duty)
                

            elif msg_type == 'LT':
                left_trigger=float(0.5)+(float(0.5)*float(value))
                if(left_trigger>0) and (right_trigger>0):
                    GPIO.output(37,GPIO.LOW) 
                    GPIO.output(38,GPIO.LOW)
                    cur_duty=int(value)
                else:
                     GPIO.output(37,GPIO.HIGH) 
                     GPIO.output(38,GPIO.LOW)
                     cur_duty=int(value)
            elif msg_type == 'RT':
                left_trigger=float(0.5)+(float(0.5)*float(value))
                if(left_trigger>0) and (right_trigger>0):
                    GPIO.output(37,GPIO.LOW) 
                    GPIO.output(38,GPIO.LOW)
                else:
                     GPIO.output(37,GPIO.LOW) 
                     GPIO.output(38,GPIO.HIGH)
                     cur_duty=float(value)



wlan0_ip=get_ip_address.get_ip_address("wlan0")
port=8888
start_server=websockets.serve(handle_websockets,str(wlan0_ip),port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
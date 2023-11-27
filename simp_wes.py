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

async def handle_websockets(websocket,path):
    

    async for message in websocket:
        if message == ' ':
            print("Yeah")
        else:
            print(f"Received: {message}")
    

wlan0_ip=get_ip_address.get_ip_address("wlan0")
port=8888
start_server=websockets.serve(handle_websockets,str(wlan0_ip),port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
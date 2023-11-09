import asyncio
import websockets
import get_ip_address


async def handle_websockets(websocket,path):
    
    async for message in websocket:
        if message.startswith("stop_record"):
            name = message.split()[1]
            print(name)
        elif message.startswith("stop_record"):
            pass
        else:
            print(f"Received: {message}")
    

wlan0_ip=get_ip_address.get_ip_address("wlan0")
port=8888
start_server=websockets.serve(handle_websockets,str(wlan0_ip),port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
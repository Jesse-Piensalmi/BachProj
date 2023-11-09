import cv2
import asyncio
import websockets
import base64

async def video_stream(websocket,path):
    cap = cv2.VideoCapture(2)
    while True:
        ret, frame = cap.read()
        frame=cv2.resize(frame, (640,480))
        if not ret:
            break

        _, frame_encoded = cv2.imencode(".jpg",frame)
        frame_base64 = base64.b64encode(frame_encoded.tobytes()).decode("utf-8")

        await websocket.send(frame_base64)

start_server = websockets.serve(video_stream, "192.168.1.56",8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

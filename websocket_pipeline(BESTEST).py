import cv2
import asyncio
import websockets
import base64
import pyrealsense2 as rs
import numpy as np
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)


async def video_stream(websocket,path):
    pipeline.start(config)
    while True:
        frames = pipeline.wait_for_frames()

        # Get the color frame
        color_frame = frames.get_color_frame()
        
        if not color_frame: #or not depth_frame:
            continue

        # Convert the color frame to an OpenCV image
        color_image = np.asanyarray(color_frame.get_data())

        _, frame_encoded = cv2.imencode(".jpg",color_image)
        frame_base64 = base64.b64encode(frame_encoded.tobytes()).decode("utf-8")

        await websocket.send(frame_base64)

start_server = websockets.serve(video_stream, "192.168.1.56",8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
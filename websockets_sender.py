import asyncio
import websockets
import cv2
import numpy as np
import sys
import pyrealsense2 as rs


# Initialize the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start the pipeline
pipeline.start(config)

# Function to capture the camera data
async def capture_camera(websocket):
    frames = pipeline.wait_for_frames()

    # Get the color frame
    color_frame = frames.get_color_frame()
    #depth_frame = frames.get_depth_frame()

    if color_frame: #or not depth_frame:
        #convert to color frame
        color_image = cv2.cvtColor(np.asanyarray(color_frame.get_data()))
        #serialize frame to bytes
        frame_data=color_image.tobytes()
        #send frame over websocket
        print("reached")
        await websocket.send(frame_data)
        print("reachest")



async def handle_websockets(websocket,path):
    #keyboard key_states
    key_states={"ArrowUp": False, "ArrowLeft": False, "ArrowRight": False, "ArrowDown": False}
    async for message in websocket:
        keys=message.decode('utf-8').split(",")
        if "q" in keys:
            #Stop the robot
            for key in keys:
                key_states[key]=False
            sys.exit()
        else:
        #update key state
            if key_states["ArrowUp"]:
                print("Yep")






#initiate the websockets for sending and receiving        
start_cam= websockets.serve(capture_camera, "192.168.1.56",8765)
start_handle=websockets.serve(handle_websockets,"192.168.1.56",8888)
    
asyncio.get_event_loop().run_until_complete(start_cam)
asyncio.get_event_loop().run_until_complete(start_handle)
asyncio.get_event_loop().run_forever()
import cv2
import pyrealsense2 as rs
import numpy as np

# Initialize the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start the pipeline
pipeline.start(config) 

try:
    while True:
        # Wait for a new frame
        frames = pipeline.wait_for_frames()

        # Get the color frame
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not color_frame: #or not depth_frame:
            continue

        # Convert the color frame to an OpenCV image
        color_image = np.asanyarray(color_frame.get_data())

        #convert the depth frame to a numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Display the frame using OpenCV
        cv2.imshow("Color view", color_image)

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03),cv2.COLORMAP_JET)
        cv2.imshow("Depth view", depth_colormap)
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release resources
    pipeline.stop()
    cv2.destroyAllWindows()
from flask import Flask, Response, render_template
import pyrealsense2 as rs
import cv2
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640,480, rs.format.bgr8, 30)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    try:
        pipeline.start(config)
        while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue

            image_data = color_frame.get_data()
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n'+cv2.imencode(".jpeg",image_data)[1].tobytes + b'\r\n')
    except Exception as e:
        print(e)
    finally:
        pipeline.stop()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary = frame')

if __name__ == '__main__':
    try:
        app.debug = True
        app.run(host="0.0.0.0",port=5000)
    except KeyboardInterrupt:
        pass
    finally:
        pass
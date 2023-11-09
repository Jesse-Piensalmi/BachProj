import socket
import cv2
import pickle
import struct
import imutils
import get_ip_address
import pyrealsense2 as rs
import numpy as np


cap = cv2.VideoCapture(2)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip=get_ip_address.get_ip_address("wlan0")
print("HOST IP: ",host_ip)
port=8888
socket_address=(host_ip,port)
print("socket created")
server_socket.bind((socket_address))
server_socket.listen(5)


while True:
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)
    if client_socket:
        
        while(cap.isOpened()):
            # Get the color frame
            #depth_frame = frames.get_depth_frame()
            ret, frame = cap.read()
            frame=cv2.resize(frame, (640,480))
            #serialize frame to bytes
            a = pickle.dumps(frame)
                
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow("Sending...",frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()
                break
                
        
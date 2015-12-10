import socket
import time
import picamera

class CameraNetwork:
  def __init__(self):
    self.camera = None
    self.server_socket = None
    self.connection = None

  def stop(self):
    self.camera.stop_recording()
    self.server_socket.close()
    self.camera.close()
    self.connection.close()
    
    
  def record(self):
    self.camera = picamera.PiCamera()
    self.camera.resolution = (640, 480)

    self.camera.framerate = 24
    self.camera.vflip = True
    
    self.server_socket = socket.socket()
    
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind(('0.0.0.0', 8001))
    self.server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    self.connection = self.server_socket.accept()[0].makefile('wb')
    self.camera.start_recording(self.connection, format='h264')

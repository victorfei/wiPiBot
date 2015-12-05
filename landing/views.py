from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
import socket
import time
import picamera
#from wiPiBotClient import *

def landing(request):
  t = get_template('index.html')
  html = t.render()

  return HttpResponse(html)


def dashboard(request):
  # used to keep track when buttons are pressed twice.
  # you keep in cruise mode
  
  t = get_template('dashboard/dashboard.html')
  html = t.render()
  camera = picamera.PiCamera()

  camera.resolution = (640, 480)
  camera.framerate = 24
  camera.vflip = True

  server_socket = socket.socket()
  server_socket.bind(('0.0.0.0', 8000))
  server_socket.listen(0)

  # Accept a single connection and make a file-like object out of it
  connection = server_socket.accept()[0].makefile('wb')
  try:
      camera.start_recording(connection, format='h264')
      camera.wait_recording(60)
      camera.stop_recording()
  finally:
      connection.close()
      server_socket.close()

  if 'cmd' in request.GET and request.GET['cmd']:
    direction = request.GET['cmd']

 #   motor_control(direction)
  
  return HttpResponse(html)


def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

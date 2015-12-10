from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from landing.models import *
from wiPiBotClient import *

def landing(request):
  t = get_template('index.html')
  html = t.render()

  return HttpResponse(html)


def dashboard(request):
  # used to keep track when buttons are pressed twice.
  # you keep in cruise mode
  
  t = get_template('dashboard/dashboard.html')

  if 'cmd' in request.GET and request.GET['cmd']:
    cmd = request.GET['cmd']

    if cmd == 'led':
      blink()

    if (cmd == 'up') or (cmd =='down'):
      speed_control(cmd)

    if cmd == 'record':
      camera.record()

    if cmd == 'stop-record':
      camera.stop()

    motor_control(cmd)

  return HttpResponse(t.render())


def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from wiPiBotClient import *

def landing(request):
  t = get_template('index.html')
  html = t.render()

  return HttpResponse(html)


def dashboard(request):
  # used to keep track when buttons are pressed twice.
  # you keep in cruise mode
  
  t = get_template('dashboard/dashboard.html')
  html = t.render()

  if 'cmd' in request.GET and request.GET['cmd']:
    direction = request.GET['cmd']

    motor_control(direction)
  
  GPIO.cleanup()
  return HttpResponse(html)


def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

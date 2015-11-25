from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template


def landing(request):
  t = get_template('index.html')
  html = t.render()

  return HttpResponse(html)


def dashboard(request):
  t = get_template('dashboard/dashboard.html')
  html = t.render()
  return HttpResponse(html)


def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

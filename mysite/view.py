from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template

import datetime

def hello(request):
    return HttpResponse("Hello World!")

def home_page(request):
    return HttpResponse("this is a blank page at %s" % request.path)

def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body> It is now %s. </body></html>" % now
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date' : now}))
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hours_ahead(request, offset): # where is offset from?
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt =  datetime.datetime.now() + datetime.timedelta(hours = offset)
    t = get_template('hours_ahead_datetime.html')
    html = t.render(Context({'hour_offset' : offset, 'next_time' : dt}))
    return HttpResponse(html)



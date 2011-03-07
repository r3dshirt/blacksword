from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404

from kin_events.models import Event

def index(request):
    events_list = Event.objects.all().order_by('-date')[:5]
    t = loader.get_template('kin_events/index.html')
    c = Context({'events_list': events_list,})
    return HttpResponse(t.render(c))
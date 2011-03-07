from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404

from blog.models import Blog

def index(request):
    recent_blog_list = Blog.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('home/index.html')
    c = Context({'recent_blog_list': recent_blog_list,})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('home/about.html')
    c = Context()
    return HttpResponse(t.render(c))
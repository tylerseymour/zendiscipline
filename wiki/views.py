from django.http import HttpResponse
from django.template import loader
from .models.node import Node

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title': "Zen Discipline",
        'description': "Welcome to Zen Discipline content library",
        'nodes': Node.objects.order_by('title')[:10]
    }
    return HttpResponse(template.render(context, request))

def app(request):
    template = loader.get_template('app.html')
    context = {
        'title': "Zen Discipline"
    }
    return HttpResponse(template.render(context, request))

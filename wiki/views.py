from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title': "Zen Discipline",
        'description': "Welcome to Zen Discipline content library"
    }
    return HttpResponse(template.render(context, request))
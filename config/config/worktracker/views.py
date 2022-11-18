from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import Members

# def index(request):
#   mymembers = Members.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["firstname"]
#   return HttpResponse(output)

def index(request):
    template = loader.get_template('home.html')
    if(request.GET.get('completed')):
        print("pressed")
    return HttpResponse(template.render())

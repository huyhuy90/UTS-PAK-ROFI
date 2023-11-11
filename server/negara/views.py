from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def asiatenggara(request):
    template = loader.get_template('asiatenggara.html')
    return HttpResponse(template.render())
def asiabarat(request):
    template = loader.get_template('asiabarat.html')
    return HttpResponse(template.render())

# Create your views here.

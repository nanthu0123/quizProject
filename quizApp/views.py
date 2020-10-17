from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name='nanthagopal'
    html=f'<h1>welcome my name is {name}.'
    return HttpResponse(html)

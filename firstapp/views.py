from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")

def helloName(request, name):
    return HttpResponse(f"Hello {name}!")
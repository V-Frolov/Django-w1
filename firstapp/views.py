from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")
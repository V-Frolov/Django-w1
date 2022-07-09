from datetime import datetime, date
from time import strftime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")


def helloName(request, name):
    return HttpResponse(f"Hello {name}!")


def show_date(request):
    return HttpResponse(datetime.now().strftime('%d.%m.%Y'))

def show_date_year(request):
    return HttpResponse(datetime.now().strftime('%Y'))

def show_date_month(request):
    return HttpResponse(datetime.now().strftime('%m'))

def show_date_day(request):
    return HttpResponse(datetime.now().strftime('%d'))

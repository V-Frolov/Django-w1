from datetime import datetime, date
from time import strftime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")


def helloName(request, name):
    return HttpResponse(f"Hello {name}!")


def showDate(request):
#    currentdate = datetime.date.today()
#    formatDate = currentdate.strftime("%d%m%Y")
#    print('Today is: ', formatDate)
    print('Data: ', datetime.now())
    return HttpResponse(datetime.now())

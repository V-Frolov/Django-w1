from django.urls import path
from .views import hellodjango, helloName, showDate

urlpatterns = [
    path('', hellodjango),
#    path("<str:name>/", helloName),
]
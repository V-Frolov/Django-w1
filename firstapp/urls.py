from django.urls import path
from .views import hellodjango, helloName

urlpatterns = [
    path('', hellodjango),
    path("<str:name>/", helloName)
]
from django.urls import path
from .views import hellodjango, helloName, show_date, show_date_year, show_date_month, show_date_day

urlpatterns = [
    path('', hellodjango),
    path('date/', show_date),
    path('date/year/', show_date_year),
    path('date/month/', show_date_month),
    path('date/day/', show_date_day),
    path("<str:name>/", helloName),
]
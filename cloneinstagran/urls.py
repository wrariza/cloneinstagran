# Django
from django.urls import path

# views
from cloneinstagran.views import say_hi, sorted_number, say_time

urlpatterns = [
    path('say_time', say_time),
    path('say-hi', say_hi),
    path('sorted-number', sorted_number)
]

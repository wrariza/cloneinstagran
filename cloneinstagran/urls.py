# Django
from django.urls import path

# views
from cloneinstagran import views as locals_views
from posts import  views as posts_views
urlpatterns = [
    path('say_time', locals_views.say_time),
    path('say-hi', locals_views.say_hi),
    path('sorted-number', locals_views.sorted_number),

    path('posts/', posts_views.list_posts)
]

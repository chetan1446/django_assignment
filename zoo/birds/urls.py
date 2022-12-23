from django.urls import path
from .views import  show_bird

urlpatterns = [
   path('show_bird/', show_bird)
]
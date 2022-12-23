from django.urls import path
from .views import show_mammals

urlpattern = [
    path('show_mammals/',show_mammals)
]
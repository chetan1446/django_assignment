from django.urls import path
from .views import show_mammal

urlpatterns = [
   path('show_mammal/',show_mammal),
]
from django.urls import path
from .views import Square, IsPalindrome,show

urlpatterns = [
    path('palindrome/',IsPalindrome),
    path('square/',Square),
    path('show/',show)
]

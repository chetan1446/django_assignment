from typing import final
from django.http.response import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here
# def Palindrome(request):
#     return HttpResponse("Palindrome")
@csrf_exempt
def show(request):
    if request.method =="GET":
        numberIs=request.GET.get("number")
    return HttpResponse(json.dumps({numberIs}),content_type='application/json')

@csrf_exempt
def IsPalindrome(request):
    if request.method =="POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        word = data['word']
        def palindrome(word):
            return word == word[::-1]
        ans = palindrome(word)
    return HttpResponse(ans)

@csrf_exempt
def Square(request):
    if request.method =="POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        number = data['number']
        Square_of_number = number*number
        value = (f"Square of {number} is {Square_of_number} ")
        print(value)
    return HttpResponse(value)



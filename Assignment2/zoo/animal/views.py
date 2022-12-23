from django.db import models
from django.shortcuts import render
from .models import Mammals
from django.http.response import HttpResponse
from django.http import HttpResponse
import json

# Create your views here.
def show_mammals(request):
    if request.method == "GET":
        all_mammals = Mammals.objects.all()
        final_data = []
        for mammal in all_mammals:
            result = {
                "name":mammal.mammals_name,
                "species":mammal.mammals_species,
                "food":mammal.mammals_food,
                "last_feed_time":mammal.mammals_feed_time
            }
            final_data.append(result)
        return HttpResponse(json.dumps({"result":final_data}),content_type='application/json')

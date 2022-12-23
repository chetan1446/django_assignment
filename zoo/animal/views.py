from django.shortcuts import render
from django.http.response import HttpResponse
import json
from .models import Mammals
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def show_mammal(request):
    if request.method == "GET":
        all_mammals = Mammals.objects.all()
        final_data= []
        for mammal in all_mammals:
            result={
                "name" : mammal.name,
                "species": mammal.species,
                "food": mammal.food,
                "last_feed_time":mammal.last_feed_time.strftime("%Y-%m-%d"),
                "gender":mammal.gender
            }
            final_data.append(result)
        return HttpResponse(json.dumps({"result":final_data}),content_type='application/json')

    if request.method =="POST":
        data = json.loads(request.body)
        name = data["name"]
        species = data["species"]
        food = data["food"]
        last_feed_time = data["last_feed_time"]
        gender = data["gender"]

        Mammals.objects.create(name = name,
                                species= species,
                                food= food,
                                last_feed_time= last_feed_time,
                                gender = gender)

        return HttpResponse(json.dumps({"result":"Mammals Added"}),content_type='application/json')

    if request.method =="PUT":
        data = Mammals.objects.get(name="silo")
        data.last_feed_time = "2021-07-23"
        data.save()
        final_data = {"message":"data updated"}
        return HttpResponse(json.dumps(final_data))

    if request.method == "DELETE":
        data = Mammals.objects.get(name="silo")
        data.delete()
        final_data = {"message":"data deleted"}
        return HttpResponse(json.dumps(final_data))

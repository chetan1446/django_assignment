
from django.http.response import HttpResponse
import json
from .models import Bird
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_bird(request):
    if request.method == "GET":
        all_bird = Bird.objects.all()
        final_bird_data = []
        for bird in all_bird:
            res={
                 "name" : bird.name,
                "species": bird.species,
                "food": bird.food,
                "last_feed_time":bird.last_feed_time.strftime("%Y-%m-%d"),
                "gender":bird.gender
            }
            final_bird_data.append(res)
        return HttpResponse(json.dumps({"res":final_bird_data}))

    
    if request.method =="POST":
        data = json.loads(request.body)
        name = data["name"]
        species = data["species"]
        food = data["food"]
        last_feed_time = data["last_feed_time"]
        gender = data["gender"]

        Bird.objects.create(name = name,
                                species= species,
                                food= food,
                                last_feed_time= last_feed_time,
                                gender = gender)

        return HttpResponse(json.dumps({"result":"Bird Added"}),content_type='application/json')

    if request.method =="PUT":
        data = Bird.objects.get(name="butterfly")
        data.last_feed_time = "2021-07-23"
        data.save()
        final_data = {"message":"data updated"}
        return HttpResponse(json.dumps(final_data))

    if request.method == "DELETE":
        data = Bird.objects.get(name="butterfly")
        data.delete()
        final_data = {"message":"data deleted"}
        return HttpResponse(json.dumps(final_data))

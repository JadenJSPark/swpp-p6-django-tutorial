from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

import json
from json.decoder import JSONDecodeError

from .models import Hero

def index(request):
    return HttpResponse('Hello, world!')

def id(request, id):
    return HttpResponse(f'Your id is {id}!')

def name(request, name):
    return HttpResponse(f'Your name is {name}!')

@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        # TODO: create a new hero
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else: 
        return HttpResponseNotAllowed(["GET", "POST"])
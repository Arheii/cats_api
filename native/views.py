import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Cat, Breed


def breeds(request):
    breeds = Breed.objects.all()
    return JsonResponse([breed.serialize() for breed in breeds], safe=False)


def cats(request):
    cats = Cat.objects.all().order_by('id')
    return JsonResponse([cat.serialize() for cat in cats], safe=False)


@csrf_exempt
def cat(request, cat_id):
    
    # Query for requested cat
    try:
        cat = Cat.objects.get(pk=cat_id)
    except Cat.DoesNotExist:
        return JsonResponse({'error': 'cat not found'}, status=404)

    # Return cat content
    if request.method == 'GET':
        print(vars(cat))
        print([attr for attr in vars(cat) if not attr.startswith('_')])
        return JsonResponse(cat.serialize(), status=200)

    # Check and update the cat parametrs
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': 'incorrect format'}, status=400)
        
        if data.get('name') is not None:
            cat.name = data['name']
        if data.get('age') is not None:
            cat.age = data['age']
        if data.get('woolliness') is not None:
            cat.woolliness = data['woolliness']
        if data.get('desc') is not None:
            cat.desc = data['desc']
        if data.get('breed') is not None:
            title = data['breed'].capitalize()
            breed_id, _ = Breed.objects.get_or_create(title=title)
            cat.breed = breed_id
        # try write new data to db and raise error if data not valid
        try:
            cat.save()
        except:
            return JsonResponse({'error': 'incorrect data'}, status=422)

        return HttpResponse(status=204)
    
    elif request.method == "DELETE":
        cat.delete()
        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "GET, PUT or DELETE request required."
        }, status=204)


@csrf_exempt
def new(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': 'incorrect format'}, status=400)
        
        cat = Cat()
        # update cat fields values
        if data.get('name') is not None:
            cat.name = data['name']
        if data.get('age') is not None:
            cat.age = data['age']
        if data.get('woolliness') is not None:
            cat.woolliness = data['woolliness']
        if data.get('desc') is not None:
            cat.desc = data['desc']
        # special handler for the breed because this is a link to Breed class
        if data.get('breed') is not None:
            title = data['breed'].capitalize()
            breed_id, _ = Breed.objects.get_or_create(title=title)
            data['breed'] = breed_id

        print(cat)
        try:
            cat.save()
        except:
            return JsonResponse({'error': 'incorrect data'}, status=400)

        return  JsonResponse({"message": "create successfully."}, status=201)

    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


from rest_framework import viewsets

from native.models import Cat, Breed
from .serializers import CatSerializer, BreedSerializer
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
class CatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cats to be viewed or edited.
    """
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows breeds to be viewed or edited.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
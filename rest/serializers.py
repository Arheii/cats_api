from native.models import Cat, Breed
from rest_framework import serializers


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    # cats = serializers.StringRelatedField(many=True)

    class Meta:
        model = Breed
        fields = ['url', 'id', 'title'] #, 'cats']


class CatSerializer(serializers.HyperlinkedModelSerializer):
    breed = serializers.StringRelatedField(many=False)
    # breed = BreedSerializer(many=False)

    class Meta:
        model = Cat
        fields = ['url', 'id', 'name', 'age', 'breed', 'woolliness', 'desc']
    
    def create(self, validated_data):
        """update default method. used get_or_create for breed field"""
        breed_data = validated_data.pop('breed').capitalize()
        breed_id, _ = Breed.objects.get_or_create(title=breed_data)
        # validated_data['breed'] = breed_id
        cat = Cat.objects.create(breed=breed_id, **validated_data)
        return cat
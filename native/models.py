from django.db import models

# Create your models here.
class Breed(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "cats": len(self.cats.all())
        }



class Cat(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, blank=True, null=True, related_name='cats')
    woolliness = models.PositiveSmallIntegerField(blank=True)
    desc = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            'name': self.name,
            'age': self.age,
            'breed': str(self.breed) if self.breed else None,
            'woolliness': self.woolliness,
            'desc': self.desc
        }
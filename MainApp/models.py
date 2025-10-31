from django.db import models

class Color(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self):
       return f'Color({self.name})'


class Item(models.Model):
    name        = models.CharField(max_length=100)
    brand       = models.CharField(max_length=100)
    count       = models.PositiveIntegerField()
    discription = models.CharField(max_length=1000) 
    colors      = models.ManyToManyField(to=Color)
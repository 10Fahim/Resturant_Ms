from django.db import models

# Create your models here.
class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cuisine_name

class Food_items(models.Model):
    item_name = models.CharField(max_length=30)
    cuisine_name = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    timing = models.CharField(max_length=20)
    price = models.IntegerField()

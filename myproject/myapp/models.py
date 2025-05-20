from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    photo=models.ImageField(upload_to="photo")

    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=255)
    section=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photo')
    def __str__(self):
        return self.name
from os import name
from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class Image(models.Model):
    
    name = models.CharField(max_length=60)
    description = models.TextField()
    image = CloudinaryField('image')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)


    def save_image(self):
        return self.save()

    def __str__(self):
        return f'Image: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
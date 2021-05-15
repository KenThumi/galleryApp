from os import name
from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class Image(models.Model):
    
    name = models.CharField(max_length=60)
    description = models.TextField()
    image = CloudinaryField('image')


    def save_image(self):
        return self.save()

    def __str__(self):
        return f'Image: {self.name}'
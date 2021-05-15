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

    @classmethod
    def update_image(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(image=update_details['image'],
                                               name=update_details['name'],
                                               description=update_details['description'],
                                               category=update_details['category'],
                                               location=update_details['location'])
        # image = Image(image=new_result if new_result else image.image,
            #                 name=form.cleaned_data['name'],
            #                 description=form.cleaned_data['description'],
            #                 category=form.cleaned_data['category'],
            #                 location = form.cleaned_data['location'] )

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
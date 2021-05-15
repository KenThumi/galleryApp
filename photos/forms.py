from django.forms import ModelForm      
from .models import Category, Image, Location
from django import forms

class ImageForm(ModelForm):
  class Meta:
      model = Image
      fields = '__all__'


class FilterLocForm(forms.Form):
    location = forms.ModelChoiceField(queryset=Location.objects.all())

       
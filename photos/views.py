from django.shortcuts import render
from .models import Image

# Create your views here.


from django.http  import HttpResponse

# Create your views here.
def home(request):
    images = Image.objects.all()

    ctx = {'images':images}
    return render(request,'index.html', ctx)
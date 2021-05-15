from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm

# Create your views here.


from django.http  import HttpResponse

# Create your views here.
def home(request):
    images = Image.objects.all()

    ctx = {'images':images}
    return render(request,'index.html', ctx)


def upload(request):
    form = ImageForm()

    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')


    ctx = {'form':form}
    return render(request,'upload.html',ctx)
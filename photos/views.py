from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm, FilterLocForm
from django.contrib import messages
import cloudinary
import cloudinary.uploader

# Create your views here.


from django.http  import HttpResponse

# Create your views here.
def home(request):
    images = Image.objects.all()

    form = FilterLocForm()

    ctx = {'images':images,'search_loc_form':form}

    return render(request,'index.html', ctx)


def upload(request):
    form = ImageForm()

    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)

        file_to_upload = request.FILES['image']
      
        if form.is_valid():
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            image = Image(image=new_result,
                          name=form.cleaned_data['name'],
                          description=form.cleaned_data['description'],
                          category=form.cleaned_data['category'],
                          location = form.cleaned_data['location'])

            image.save_image()

            messages.success(request, 'Successful upload.')
            return redirect('home')


    ctx = {'form':form}
    return render(request,'upload.html',ctx)


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text 



def edit(request,image_id):
    image = Image.objects.get(pk=int(image_id))

    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)
    
        try:
            file_to_upload = request.FILES['image']
        except:
            messages.error(request, 'Kindly select an image.')
           
      
        if form.is_valid():
            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            image_result = new_result if new_result else image.image

            update_details = {'image':image_result,
                               'name':form.cleaned_data['name'],
                                'description':form.cleaned_data['description'],
                                'category':form.cleaned_data['category'],
                                'location':form.cleaned_data['location'] }

            Image.update_image(update_details,image_id)

            messages.success(request, 'Successful edit.')
            return redirect('home')



    form = ImageForm(instance=image)

    ctx = {'form':form}

    return render(request,'upload.html',ctx)



def search_category(request):

    if request.method=='POST':

        needle = request.POST['search']

        images=Image.search_category(needle)

        ctx = {'images':images, 'search_results':f'Search Results ({images.count()})'}

    
        return render(request,'index.html', ctx)

    return redirect('home')


def filter_by_location(request):
    if request.method == 'POST':
        needle = request.POST['location']

        images = Image.filter_by_location(needle)

        ctx = {'images':images, 'search_results':f'Search Results ({images.count()})'}

    
        return render(request,'index.html', ctx)

    return redirect('home')


def copy_image_url(request,image_id):
    image = Image.objects.get(pk=int(image_id))

    image.copy_image_url()

    messages.success(request, 'Image URL copied successfully.')
    
    return redirect('home')


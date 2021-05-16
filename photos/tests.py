from os import name
import cloudinary
from django.test import TestCase
from .models import Image,Category,Location
import pyperclip
# Create your tests here.


class ImageTestClass(TestCase):
    '''Test methods of Image model'''

    def setUp(self):
        self.category = Category(name='Race')
        self.location = Location(name='Africa')
        self.image=Image(image='imageurl.png',name='Test Image',description='Lorem ipsum',category=self.category,location=self.location)

    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


    def test_save_image(self):
        self.category.save()
        self.location.save()
        self.image.save()

        images = Image.objects.all()

        self.assertTrue(len(images)>0)


    def test_update_image(self):
        self.category.save()
        self.location.save()
        self.image.save()

        update_details = {'image':'newlink.png',
                               'name':'image_name',
                                'description':'some image description',
                                'category':self.category,
                                'location':self.location }


        Image.update_image(update_details, self.image.id)

        self.updated_image = Image.objects.get(pk = self.image.id) #get new updated image

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(self.updated_image.image.url, cloudinary_url_prefix+'newlink.png')



    def test_search_category(self):
        self.category.save()
        self.location.save()
        self.image.save()

        self.search_results = Image.search_category('Race')

        self.assertTrue( self.search_results.count() > 0 )


    def test_filter_by_location(self):
        self.category.save()
        self.location.save()
        self.image.save()

        self.filter_results = Image.filter_by_location(self.location)

        self.assertTrue( self.filter_results.count() > 0 )


    def test_copy_image_url(self):
        self.category.save()
        self.location.save()
        self.image.save()

        self.image = Image.objects.get(pk=self.image.id)

        self.image.copy_image_url()

        cloudinary_url_prefix = 'http://res.cloudinary.com/dtw9t2dom/image/upload/'

        self.assertEqual(pyperclip.paste(), cloudinary_url_prefix+'imageurl.png')




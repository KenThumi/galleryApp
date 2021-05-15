from django.test import TestCase
from .models import Image
# Create your tests here.


class ImageTestClass(TestCase):
    '''Test methods of Image model'''

    def setUp(self):
        self.image=Image(image='imageurl.png',name='Test Image',description='Lorem ipsum')

    
    def tearDown(self):
        Image.objects.all().delete()


    def test_save_image(self):
        self.image.save()

        images = Image.objects.all()

        self.assertTrue(len(images)>0)
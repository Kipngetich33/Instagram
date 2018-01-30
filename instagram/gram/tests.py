from django.test import TestCase
from . models import Image

class ImageTestClass(TestCase):
    '''
    A class that test the Image class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.image = Image(image = 'image_url',image_name ='vin' , image_caption='hey there',)

    def test_instance(self):
        '''
        method that test is image objects are instanciated correctly
        '''
        self.assertTrue(isinstance(self.image,Image)) 


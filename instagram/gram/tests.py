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

    def test_save_image(self):
        '''
        method that test the save method of model image
        '''
        self.image.save_image()
        all_images= Image.objects.all()
        self.assertTrue(len(all_images)>0)

    def test_delete_images(self):
        '''
        method that tests the delete_images method
        '''
        self.image.save_image()
        new_image = Image(image = 'image_url2',image_name ='vin2' , image_caption='hey there2',)
        new_image.save_image()
        self.image.delete_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images)==1)

    def test_update_caption(self):
        '''
        method that tests the update caption
        '''
        self.image.save_image()
        image = Image.objects.get(image ='image_url')
        image.update_caption('new caption')
        image = Image.objects.get(image ='image_url')
        self.assertTrue(image.image_caption=='new caption')

    def test_get_image_by_id(self):
        '''
        method that tests the get image by id function of image model
        '''
        pass




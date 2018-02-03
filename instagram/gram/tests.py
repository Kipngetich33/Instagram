from django.test import TestCase
from . models import Image, Profile, Comment, Like

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


class ProfileTestClass(TestCase):
    '''
    class that test the characteristics of the Profile model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.profile = Profile(profile_photo ='test_profile_photo', bio = 'test_bio')

    def test_save_profile(self):
        '''
        method that tests save method of the Profile model
        '''
        self.profile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles)>0)

        
    def test_delete_profile(self):
        '''
        method that tests the delete_profile method
        '''
        self.profile.save_profile()
        profile2 = Profile(profile_photo ='test_profile_photo2',bio = 'test_bio2')
        profile2.save_profile()
        self.profile.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles)==1)

    def test_find_profile(self):
        '''
        method that tests the find_profile method
        '''
        self.profile.save_profile()
        profile2 = Profile(profile_photo ='test_profile_photo2',bio = 'test_bio2')
        profile2.save_profile()
        search_profile = Profile.find_profile('test_bio2')
        self.assertTrue(len(search_profile)==1)

class CommentTestClass(TestCase):
    '''
    class that test the characteristics of the Comment model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.new_comment = Comment(comment= "this is a test comment")
        self.new_comment.save()

    def test_instance(self):
        '''
        Test that checks if the created comment is an instance of the class Comment
        '''
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        '''
        method that tests save method of the Comment model
        '''
        self.new_comment.save_comment()
        all_comments = Comment.objects.all()
        self.assertTrue(len(all_comments)>0)

        
    def test_delete_comment(self):
        '''
        method that tests the delete_profile method
        '''
        self.new_comment.save_comment()
        comment2 = Comment(comment='this is the seconf test comment')
        comment2.save_comment()
        self.new_comment.delete_comment()
        all_comments = Comment.objects.all()
        self.assertTrue(len(all_comments)==1)

class LikesTestClass(TestCase):
    '''
    class that test the characteristics of the Comment model
    '''

    def setUp(self):
        '''
        Method that runs at the beggining of each test
        '''
        self.new_like = Like (likes_number=0) 

    def test_instance(self):
        '''
        Test whether an object is an instance of class Like
        '''
        self.assertTrue(isinstance(self.new_like, Like))

    def test_save_like(self):
        '''
        Test whether the save_likes method works
        '''
        self.new_like.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes)>0)

    def test_unlike(self):
        self.new_like.save_like()
        self.new_like.unlike()
        like_status = self.new_like.likes_number
        self.assertTrue(like_status == 1)

    def test_like(self):
        self.new_like.save_like()
        self.new_like.like()
        like_status = self.new_like.likes_number
        self.assertTrue(like_status == 2)

    
    

    






   



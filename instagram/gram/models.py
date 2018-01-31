from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    class that defines the structure of each profile object
    '''
    profile_photo = models.ImageField(upload_to="images/")
    bio = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def find_profile(cls,name):
        found_profiles = cls.objects.filter(bio__icontains = name).all()
        return found_profiles

class Image(models.Model):
    image = models.ImageField(upload_to="images/",blank = True)
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True, null= True)
    profile_key = models.ForeignKey(Profile,on_delete=models.CASCADE , null= True)
    user_key = models.ForeignKey(User,on_delete= models.CASCADE, null= True )

    def __str__(self):
        return self.image_name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete() 

    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()





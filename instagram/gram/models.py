from django.db import models

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="images/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.bio 

class Image(models.Model):
    image = models.ImageField(upload_to="images/",blank = True)
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField(blank=True)
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True, null= True)

    def __str__(self):
        return self.image_name 




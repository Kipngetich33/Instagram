from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField(blank=True)
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="images/")
    bio = models.TextField(blank=True)
    user_key = models.ForeignKey(User ,on_delete=models.CASCADE)


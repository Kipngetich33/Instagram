from django.db import models

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="images/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to="images/",blank = True)
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField(blank=True)
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True, null= True)

    def __str__(self):
        return self.image_name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete() 

    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()





from django import forms
from . models import Image, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm


class ImageForm(forms.ModelForm): 
    '''
    class that creates and image upload form
    '''
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']

class CommentForm(forms.ModelForm):
    '''
    class that creates the comment form
    '''
    class Meta:
        model = Comment
        fields = ['comment']

class ProfileUpdateForm(forms.Form):
    '''
    classs that creates profile update form
    ''' 
    profile_photo = forms.ImageField(label='Image')
    bio = forms.CharField(label='Image Caption',max_length=500)

class UpdateImageCaption(forms.Form):
    '''
    class that creates the caption update form
    '''
    image_caption = forms.CharField(label='Image Caption',max_length=300)


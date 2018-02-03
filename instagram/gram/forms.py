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

class ProfileUpdateForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']  


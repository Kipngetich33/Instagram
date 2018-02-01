from django import forms
from . models import Image, Comment
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


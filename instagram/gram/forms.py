from django import forms
from . models import Image

class NewsLetterForm(forms.Form):
    image_name = forms.CharField(label='Image Name',max_length=30)
    image_caption = forms.CharField(label='Image Name',max_length=300)
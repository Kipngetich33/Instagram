from django.http  import Http404
from django.shortcuts import render,redirect
from . models import Image ,Profile, Like
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . forms import ImageForm, CommentForm, ProfileUpdateForm
import os

@login_required(login_url='/accounts/login/')
def timeline(request):
    date = dt.date.today()
    timeline_images = Image.get_all_images()
    likes = Like.get_likes()
    return render(request, 'all-grams/timeline.html',{"date":date,"timeline_images":timeline_images, "likes":likes}) 

def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_name = request.GET.get("name")
        found_users = Profile.find_profile(search_name)
        message =f"{search_name}"

        return render(request,'all-grams/search_results.html',{"message":message,"found_users":found_users})
    else:
        message = "Please enter a valid username"
    return render(request,'all-grams/search_results.html',{"message":message})

def single_user(request,user_id):
    try:
        user = Profile.objects.get(id=user_id)
    except:
        raise Http404()
    return render(request,'all-grams/single.html',{"user":user})

def single_image(request,image_id):
    try:
        image = Image.objects.get(id= image_id)
    except:
        raise Http404()
    return render(request, 'all-grams/single_image.html',{"image":image})

def post(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.save() 

            return redirect( timeline)
    else:
        form = ImageForm()
    return render(request, 'all-grams/post.html',{"form" : form}) 

def comment(request, image_id):
    current_image = Image.objects.get(id=image_id)
    current_user = request.user

    if request.method == 'POST':

        form = CommentForm(request.POST)
        logger_in = request.user

        if form.is_valid():
            comment = form.save(commit = False)
            comment.user_id= current_user
            comment.image_id = current_image

            comment.save() 
            return redirect(timeline)
    else:
        form = CommentForm()
    return render(request,'all-grams/comment.html',{"form":form})  

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user 
    title = 'Update Profile'

    current_user = request.user

    if request.method == 'POST':

        form = ProfileUpdateForm(request.POST ,request.FILES)

        if form.is_valid():
            new_profile = form.save(commit = False)
            new_profile.user = current_user.id
            new_profile.save() 

            return redirect( timeline)
    else:
        form = ImageForm()

    return render(request,'profile/update_profile.html',{"title":title,"current_user":current_user,"form":form})

def profile(request):
    title = 'Profile'
    current_user = request.user
    profile = Profile.objects.get(user_id = current_user) 
    return render(request, 'profile/profile.html',{"profile":profile,"current_user":current_user})


def more(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,'all-grams/more.html',{"image":image}) 


def like(request):
    pass

def test(request):
    return render(request, 'all-grams/test.html')






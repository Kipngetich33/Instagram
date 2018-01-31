from django.http  import Http404
from django.shortcuts import render,redirect
from . models import Image ,Profile
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

@login_required(login_url='/accounts/login/')
def timeline(request):
    date = dt.date.today()
    return render(request, 'all-grams/timeline.html',{"date":date}) 

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
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'all-grams/post.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'all-grams/post.html')
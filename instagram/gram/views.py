from django.http  import Http404
from django.shortcuts import render,redirect
from . models import Image ,Profile
import datetime as dt

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
        user = User.objects.get(id=user_id)
    except:
        raise Http404()
    return render(request,'all-grams/single_user.html',{"user":user})
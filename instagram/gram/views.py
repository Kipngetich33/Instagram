from django.shortcuts import render,redirect
import datetime as dt

def timeline(request):
    date = dt.date.today()
    return render(request, 'all-grams/timeline.html',{"date":date}) 


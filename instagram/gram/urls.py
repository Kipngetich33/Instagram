from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.timeline,name = 'timeline'),
    url(r'^search/', views.search_results, name='search_results')
]
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.timeline,name = 'timeline'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/(\d+)', views.single_user, name='single_user'),
    url(r'^image/(\d+)', views.single_image, name='single_image'), 
    url(r'^post/', views.post, name='post'),
    url(r'^comment/(\d+)', views.comment, name='comment'),
    url(r'^test/', views.test, name='test'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
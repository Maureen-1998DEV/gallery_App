from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.main_gallery,name = 'main_gallery'),
    url(r'^location/(\d+)',views.location,name = 'location'),
    url(r'^search/',views.search,name='search'),
    url(r'^image/(?P<category>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
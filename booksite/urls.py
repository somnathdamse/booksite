from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name ='home'),
    path('contact', views.contact, name ='contact'),
    path('about', views.about, name ='About'),
    path('signup', views.signup, name ='signup'),
    path('contactprocess', views.contactprocess, name ='contactprocess'),
    path('upload', views.upload, name ='upload'),
    path('search', views.search, name ='search')
]


    # path('upload', views.upload, name ='upload')

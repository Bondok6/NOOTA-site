from django.conf.urls import url
from django.urls import path
from . import views  #views in the same folder (.)

app_name ='home'
urlpatterns = [
    url(r'^$' , views.allnotes , name='allnotes'), #go to views funcName all_ntes.
    url(r'^(?P<slug>[-\w]+)/$' , views.notedetails , name='notedetails'),
    #path('home', views.allnotes, name='allnotes'),

]

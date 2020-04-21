from django.conf.urls import url
from django.urls import path
from . import views  #views in the same folder (.)

app_name ='note_app'
urlpatterns = [
    url(r'^$' , views.all_notes , name='all_notes'), #go to views funcName all_ntes.
    url(r'^(?P<slug>[-\w]+)/$' , views.detail , name='note_detail'),
    url(r'^add$' , views.note_add , name='add_note'),
    url(r'^(?P<slug>[-\w]+)/edit$' , views.edit , name='note_edit'),
    url(r'^(?P<slug>[-\w]+)/delete$' , views.delete , name='note_delete'),
]

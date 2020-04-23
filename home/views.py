from django.shortcuts import render , get_object_or_404
from notes_app.models import Note
from accounts.models import Profile
# Create your views here.



def allnotes(request):
    notes = Note.objects.all()
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile , user=user)

        context ={
            'all_notes': notes ,
            'profile': profile ,
        }
    else:
        context ={
            'all_notes': notes ,
        }
    return render(request , 'home.html' , context)


def notedetails(request,slug):
        user = request.user
        profile = get_object_or_404(Profile , user= user)
        note = Note.objects.get(slug=slug)
        context ={
            'note':note ,
            'profile' : profile ,
        }
        return render(request , 'note_details.html', context)

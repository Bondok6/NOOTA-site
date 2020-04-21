from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from accounts.models import Profile

# Create your views here.

#show all notes
def all_notes(request):
    user = request.user
    profile = get_object_or_404(Profile , user= user)
    all_notes = Note.objects.filter(user=user)

    context ={
    'all_notes' : all_notes ,
    'profile' : profile ,
    }
    return render(request, 'notes.html' , context )


#show one note details
def detail(request,slug):
    user = request.user
    profile = get_object_or_404(Profile , user= user)
    note = Note.objects.get(slug=slug)
    context ={
        'note':note ,
        'profile' : profile ,
    }
    return render(request , 'one_note.html', context)



def note_add(request):
    user = request.user
    profile = get_object_or_404(Profile , user= user)
    if request.method == 'POST':
        form = NoteForm(request.POST,request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.add_message(request, messages.INFO, 'Note Added Successfully')
            return redirect('/notes')

    else :
        form = NoteForm()

    context ={
        'form' : form ,
        'profile' : profile ,
    }
    return render(request , 'add.html' , context)


def edit(request,slug):
        user = request.user
        profile = get_object_or_404(Profile , user= user)
        note = get_object_or_404(Note,slug=slug)
        if request.method == 'POST':
            form = NoteForm(request.POST,request.FILES,instance = note)

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()
                messages.add_message(request, messages.INFO, 'Note Updated Successfully')
                return redirect('/notes')

        else :
            form = NoteForm(instance = note)

        context ={
            'form' : form ,
            'profile' : profile ,
        }
        return render(request , 'create.html' , context)



def delete(request,slug):
    item = get_object_or_404(Note ,slug=slug)
    item.delete()
    messages.add_message(request, messages.INFO, 'Note Deleted Successfully')
    return redirect('/notes')

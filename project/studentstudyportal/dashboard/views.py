from django.shortcuts import render
from . forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            note.save()

        messages.success(request,f"Notes added from {request.user.username}Successfully")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)

    #context = {'notes' :notes, 'form': form}
    
   # return render(request,'dashboard/notes.html',context)
    return render(request, 'dashboard/notes.html', {'notes': notes, 'form': form})


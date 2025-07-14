from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
import json
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
    posts = [{'title': 'Sample Post 01', 'content': '01 This is a sample post content.'},
             {'title': 'Sample Post 02', 'content': '02 This is a sample post content.'},
             {'title': 'Sample Post 03', 'content': '03 This is a sample post content.'},
             {'title': 'Sample Post 04', 'content': '04 This is a sample post content.'},
             {'title': 'Sample Post 05', 'content': '05 This is a sample post content.'},]
    """ 01
    Render the home page of the notebook application.
    """
    return render(request, 'notes/home.html',context={'posts': posts})

@login_required
def index(request):
    notes = Note.objects.filter(author=request.user).order_by('-updated_at')
    return render(request, 'notes/index.html',context={'notes': notes})

@login_required
def delete_note(request):
    """Delete a note entry."""
    if request.method == 'POST':
        data = json.loads(request.body)
        note_id = data.get('note_id')
        try:
            note = Note.objects.get(id=note_id, author=request.user)
            note.delete()
            messages.success(request, f'Notebook deleted successfully.')
        except Note.DoesNotExist:
            messages.error(request, f'Notebook not found.')
    notes = Note.objects.all().order_by('-updated_at')
    return render(request, 'notes/index.html',context={'notes': notes})


@login_required
def update_note(request, note_id):
    """Update a notebook entry."""
    note = get_object_or_404(Note, id=note_id, author=request.user)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notes:home')

    return render(request, 'notes/update.html', {'note': note})

@login_required
def save_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notes:home')  # Redirect after saving

    return render(request, 'notes/update.html', {'note': note})
    
@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content, author=request.user)
        return redirect('notes:home')
    return render(request, 'notes/create.html')
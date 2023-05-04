from django.shortcuts import render, get_object_or_404
from recette.models import Recette
from etapes.models import Etape
from notes.models import Note
from commentaires.models import Commentaire
from django.db import models
from notes.forms import NoteForm
from django.contrib.auth.decorators import login_required


@login_required
def ajouter_note(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.recette = recette
            note.user = request.user
            note.save()
            return redirect('detail_recette', pk=pk)
    else:
        form = NoteForm()
    context = {'form': form}
    return render(request, 'ajouter_note.html', context)

def detail_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    etapes = Etape.objects.filter(recette=recette).order_by('ordre')
    note_moyenne = Note.objects.filter(recette=recette).aggregate(models.Avg('valeur'))['valeur__avg']
    commentaires = Commentaire.objects.filter(recette=recette).order_by('-date')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.recette = recette
            note.user = request.user
            note.save()
            return redirect('detail_recette', pk=pk)
    else:
        form = NoteForm()
    context = {
        'recette': recette,
        'etapes': etapes,
        'note_moyenne': note_moyenne,
        'commentaires': commentaires,
        'form': form
    }
    return render(request, 'detail_recette.html', context)
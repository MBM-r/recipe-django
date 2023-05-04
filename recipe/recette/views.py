from django.shortcuts import render, get_object_or_404
from recette.models import Recette
from etapes.models import Etape
from notes.models import Note
from commentaires.models import Commentaire
from django.db import models


def detail_recette(request, pk):
    # Récupérer la recette spécifique avec l'ID (pk)
    recette = get_object_or_404(Recette, pk=pk)

    # Récupérer les étapes associées à la recette
    etapes = Etape.objects.filter(recette=recette).order_by('ordre')

    # Récupérer la note moyenne pour la recette
    note_moyenne = Note.objects.filter(recette=recette).aggregate(models.Avg('valeur'))['valeur__avg']

    # Récupérer les commentaires pour la recette
    commentaires = Commentaire.objects.filter(recette=recette).order_by('-date')

    context = {
        'recette': recette,
        'etapes': etapes,
        'note_moyenne': note_moyenne,
        'commentaires': commentaires,
    }

    return render(request, 'detail_recette.html', context)


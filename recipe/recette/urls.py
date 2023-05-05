from django.urls import path
from . import views
from .views import ajouter_commentaire

urlpatterns = [
    # Autres URLs de l'application
    path('recette/<int:pk>/', views.detail_recette, name='detail_recette'),
    path('<int:pk>/ajouter_commentaire/', ajouter_commentaire, name='ajouter_commentaire'),

]
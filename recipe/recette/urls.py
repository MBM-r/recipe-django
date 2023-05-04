from django.urls import path
from . import views

urlpatterns = [
    # Autres URLs de l'application
    path('recette/<int:pk>/', views.detail_recette, name='detail_recette'),
]

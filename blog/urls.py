
from django.urls import path
from .views import ListePoste, Detailposte, CreerPoste, ModifierPoste, Supprimerposte

urlpatterns = [
    path('', ListePoste.as_view(), name='liste_poste'), 
    path('<int:pk>/', Detailposte.as_view(), name='detail_poste'), 
    path('create/', CreerPoste.as_view(), name='creer_poste'), 
    path('<int:pk>/modifier/', ModifierPoste.as_view(), name='modifier_poste'), 
    path('<int:pk>/supprimer/', Supprimerposte.as_view(), name='supprimer_poste'), 
]

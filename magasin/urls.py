from django.urls import path
from . import views
from rest_framework import routers
from .views import CategoryAPIView
from .views import ProduitAPIView 
from magasin.views import ProductViewset,CategoryAPIView
router = routers.SimpleRouter() 
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
    path('', views.index, name='index'),
     path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
      path('nouvCommande/', views.nouveauCommande, name='nouveauCommande'),
     path('register/',views.register, name = 'register'), 
     path('api/category/', CategoryAPIView.as_view()) ,
     path('api/produit/', ProduitAPIView.as_view()) ,
     

     

]

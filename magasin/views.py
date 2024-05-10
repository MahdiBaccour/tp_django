from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from magasin.serializers import CategorySerializer
from magasin.serializers import ProductSerializer
from magasin.models import Categorie
from django.template import loader
from django.http import HttpResponseRedirect
from rest_framework import viewsets 
from django.template import loader
from .models import produits
from .models import command
from .forms import ProduitForm 
from .forms import FournisseurForm
from .forms import commandForm
from .models import Fournisseur
from django.shortcuts import redirect
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def index1(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html',context)
def index(request):
    
    if request.method=="POST":
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
        return HttpResponseRedirect('/magasin')
    else : 
            """form = ProduitForm() #créer formulaire vide"""
            list=produits.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})
def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')
    else:
        form = FournisseurForm()
    
    fournisseurs = Fournisseur.objects.all()
    
    return render(request, 'magasin/fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})
def nouveauCommande(request):
    if request.method == 'POST':
        form = commandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauCommande')
    else:
        form = commandForm()
    
    commands = command.objects.all()
    
    
    return render(request, 'magasin/commande.html', {'form': form, 'commands': commands})
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})

def logout(request): 
    logout(request)
class CategoryAPIView(APIView): 
    def get(self, *args, **kwargs): 
        categories = Categorie.objects.all() 
        serializer = CategorySerializer(categories, many=True) 
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produit = produits.objects.all()
        serializer =ProductSerializer(produit, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet): 
    serializer_class = ProductSerializer
    def get_queryset(self): 
        queryset = produits.objects.filter() 
        category_id = self.request.GET.get('catégorie_id') 
        if category_id: 
            queryset = queryset.filter(categorie_id=category_id) 
        return queryset 
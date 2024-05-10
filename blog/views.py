from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PosteForm
from .models import Post
class ListePoste(ListView):
    model = Post
    template_name = 'blog/liste_poste.html'
    context_object_name = 'postes'
class Detailposte(DetailView):
    model = Post
    template_name = 'blog/detail_poste.html'
    context_object_name = 'produit'
class CreerPoste(CreateView):
    model = Post
    template_name = 'blog/creer_poste.html'
    form_class = PosteForm
    success_url = reverse_lazy('liste_poste') 
class ModifierPoste(UpdateView):
    model = Post
    template_name = 'blog/modifier_poste.html'
    form_class = PosteForm
    success_url = reverse_lazy('liste_poste') 
class Supprimerposte(DeleteView):
    model = Post
    template_name = 'blog/supprimer_poste.html'
    success_url = reverse_lazy('liste_poste') 

# Create your views here.

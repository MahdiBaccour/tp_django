from django.forms import ModelForm
from .models import produits
from .models import Fournisseur
from .models import command
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProduitForm(ModelForm):
    class Meta:
        model=produits
        fields=['libelle','description']
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'
class commandForm(ModelForm):
    class Meta:
        model = command
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
        
from rest_framework.serializers import ModelSerializer 
from magasin.models import Categorie 
from magasin.models import produits
class CategorySerializer(ModelSerializer): 
    class Meta: 
        model = Categorie 
        fields = ['id', 'name'] 

class ProductSerializer(ModelSerializer):
    class Meta:
        model = produits
        fields = ['id', 'libelle', 'description', 'catégorie']
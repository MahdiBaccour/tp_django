from django.contrib import admin

# Register your models here.
from .models import produits, produits
from .models import Categorie
from .models import Fournisseur
from .models import ProduitNC
from .models import command

admin.site.register(produits)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(command)

from sre_parse import CATEGORIES
from django.db import models
from datetime import date
# Create your models here.
class Categorie(models.Model):
    type_choices=[('AL','Alimentaire'),('Mb','Meuble'),('SN','Sanitaire'),('Vs','Vaisselle'),('Vt','Vetement'),('Jx','Jouets'),('Lg','Linge de maison'),('Bj','Bijoux'),('Dc','Decor'),('F','Frais'),('El','Electroménager'),('im','immobilier'),('par','parapharmacie'),('tp','tapis')]    
    name=models.CharField(max_length=50,choices=type_choices)
    def __str__(self) :
        return self.name
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='tunis')
    email=models.EmailField(default='mail')
    telephone=models.CharField(max_length=8)
    def __str__(self) :
        
        return self.nom+" "+self.adresse+" "+self.email+" "+self.telephone
class produits(models.Model):
    type_choices=[('em','emballe'),('fr','frais'),('es','conserve')]
    libelle=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=type_choices)
    img=models.ImageField(blank=True)
    catégorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
    def __str__(self) :
        
        return self.libelle+" "+self.description+" "+str(self.prix)+" "+self.type
class ProduitNC(produits):
    Duree_garantie=models.CharField(max_length=100)
class command(models.Model):
    DateCde=models.DateField(null=True,default=date.today)
    totalcde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(produits)
    def __str__(self) :
        
        return str(self.DateCde)+" "+str(self.totalcde)+" "+self.produits
    def calcul(self):
        return sum(produits.prix for produits in self.produits.all())




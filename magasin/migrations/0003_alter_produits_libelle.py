# Generated by Django 5.0.2 on 2024-02-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_produits_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produits',
            name='libelle',
            field=models.CharField(max_length=100),
        ),
    ]

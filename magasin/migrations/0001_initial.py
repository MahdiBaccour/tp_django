# Generated by Django 5.0.2 on 2024-02-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=2)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=3, max_digits=10)),
                ('type', models.CharField(choices=[('em', 'emballe'), ('fr', 'frais'), ('es', 'conserve')], max_length=2)),
            ],
        ),
    ]

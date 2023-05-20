# Generated by Django 4.2.1 on 2023-05-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('titulo_original', models.CharField(max_length=100, verbose_name='Titulo original')),
                ('url_imagen', models.CharField(max_length=300, verbose_name='Url imagen')),
                ('fecha_estreno', models.CharField(max_length=15, verbose_name='Url imagen')),
                ('sinopsis', models.CharField(max_length=500, verbose_name='Sinopsis')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-09 23:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('contenido', models.TextField()),
                ('imagenPrincipal', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('imagenSecundaria', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('imagenTerciaria', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('videoPrincipal', models.URLField(blank=True, null=True)),
                ('videoSecundario', models.URLField(blank=True, null=True)),
                ('videoTerciario', models.URLField(blank=True, null=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaActualizacion', models.DateTimeField(auto_now=True)),
                ('publicado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.categoria')),
            ],
        ),
    ]

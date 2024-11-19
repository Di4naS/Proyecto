# Generated by Django 5.1.1 on 2024-11-18 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_producto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='home.categoria'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.marca'),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-05 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_rutaimagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rutaImagen',
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
    ]

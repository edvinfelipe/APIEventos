# Generated by Django 2.2.5 on 2019-09-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLocalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoLocalidad', models.CharField(max_length=45)),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-23 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localidades', '__first__'),
        ('eventos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroAsiento', models.CharField(max_length=6)),
                ('disponible', models.BooleanField()),
                ('idEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
                ('idLocalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad')),
            ],
        ),
    ]
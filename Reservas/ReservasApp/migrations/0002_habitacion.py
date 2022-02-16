# Generated by Django 4.0.2 on 2022-02-14 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descipcion', models.CharField(max_length=60)),
                ('tipohabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservasApp.tipohabitacion')),
            ],
        ),
    ]

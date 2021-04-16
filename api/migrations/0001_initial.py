# Generated by Django 3.2 on 2021-04-13 20:56

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('author', models.CharField(max_length=100)),
                ('creationDate', models.DateTimeField()),
                ('updateDate', models.DateTimeField()),
                ('state', models.CharField(choices=[('Por Validar', 'Por Validar'), ('Validado', 'Validado'), ('Resolvido', 'Resolvido')], default='Por Validar', max_length=50)),
                ('category', models.CharField(choices=[('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'), ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION')], default='INCIDENT', max_length=50)),
            ],
        ),
    ]

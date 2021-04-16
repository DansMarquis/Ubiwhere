# Generated by Django 3.2 on 2021-04-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='category',
            field=models.CharField(choices=[('CONSTRUCTION', 'CONSTRUCTION'), ('SPECIAL_EVENT', 'SPECIAL_EVENT'), ('INCIDENT', 'INCIDENT'), ('WEATHER_CONDITION', 'WEATHER_CONDITION'), ('ROAD_CONDITION', 'ROAD_CONDITION')], max_length=50),
        ),
    ]

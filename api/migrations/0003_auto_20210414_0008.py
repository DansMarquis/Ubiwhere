# Generated by Django 3.2 on 2021-04-13 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_occurrence_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 0, 8, 59, 176375)),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='updateDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 0, 8, 59, 176375)),
        ),
    ]
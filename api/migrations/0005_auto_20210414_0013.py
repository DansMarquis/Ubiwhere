# Generated by Django 3.2 on 2021-04-13 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210414_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 0, 13, 38, 171371)),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='updateDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 0, 13, 38, 171371)),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-29 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('garbageday', '0003_auto_20191128_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garbageday',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House'),
        ),
    ]

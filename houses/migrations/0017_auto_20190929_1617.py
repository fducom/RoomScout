# Generated by Django 2.2.4 on 2019-09-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0016_auto_20190929_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='street_number',
            field=models.CharField(default='', max_length=400),
        ),
    ]

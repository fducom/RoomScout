# Generated by Django 2.2.4 on 2019-09-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bills', '0009_auto_20190902_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]

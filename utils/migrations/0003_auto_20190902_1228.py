# Generated by Django 2.2.4 on 2019-09-02 16:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('utils', '0002_auto_20190814_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatefile',
            old_name='upload',
            new_name='file',
        ),
    ]

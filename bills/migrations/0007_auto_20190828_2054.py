# Generated by Django 2.2.4 on 2019-08-29 00:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bills', '0006_auto_20190828_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billset',
            old_name='month',
            new_name='date',
        ),
    ]

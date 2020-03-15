# Generated by Django 2.2.4 on 2019-09-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rooms', '0014_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_accessible',
            field=models.BooleanField(default=False, help_text='House is accessible with ramp or elevator', verbose_name='Accessible'),
        ),
        migrations.AddField(
            model_name='room',
            name='open_to_students',
            field=models.BooleanField(default=True, help_text='Students are free to inquire about rooms at this house'),
        ),
        migrations.AddField(
            model_name='room',
            name='pets_allowed',
            field=models.BooleanField(default=False, help_text='Pets are allowed'),
        ),
    ]

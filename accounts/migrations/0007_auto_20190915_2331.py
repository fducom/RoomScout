# Generated by Django 2.2.4 on 2019-09-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0006_phonenumberverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bill_contact',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='promo_contact',
            field=models.BooleanField(default=False),
        ),
    ]

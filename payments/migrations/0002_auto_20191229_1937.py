# Generated by Django 2.2.9 on 2019-12-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-12 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='fingerprint',
            name='ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='security.IP'),
        ),
    ]

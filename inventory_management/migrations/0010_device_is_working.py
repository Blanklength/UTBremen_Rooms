# Generated by Django 4.0.5 on 2022-06-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0009_alter_location_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_working',
            field=models.BooleanField(default=True, verbose_name='Funktionsfähig?'),
        ),
    ]
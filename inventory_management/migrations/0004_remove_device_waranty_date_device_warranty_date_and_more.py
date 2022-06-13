# Generated by Django 4.0.5 on 2022-06-10 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='waranty_date',
        ),
        migrations.AddField(
            model_name='device',
            name='warranty_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Garantie Ablauf Datum'),
        ),
        migrations.AlterField(
            model_name='device',
            name='production_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Produktions Datum'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-10 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0005_room_devices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='devices',
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_management.room', verbose_name='Raum'),
        ),
    ]
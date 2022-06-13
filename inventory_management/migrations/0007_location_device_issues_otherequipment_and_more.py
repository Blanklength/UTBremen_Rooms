# Generated by Django 4.0.5 on 2022-06-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_remove_room_devices_device_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(choices=[('BA1', 'Bauabschnitt 1'), ('BA2', 'Bauabschnitt 2')], default='Bauabschnitt 1', max_length=10)),
                ('floor', models.CharField(choices=[('BST', 'Basement'), ('GF', 'Ground Floor'), ('1F', 'First Floor'), ('2F', 'Second Floor')], default='1F', max_length=10)),
            ],
            options={
                'verbose_name': 'Ort',
                'verbose_name_plural': 'Orte',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='issues',
            field=models.CharField(blank=True, default='keine Fehler', max_length=50, verbose_name='Geräte Fehler'),
        ),
        migrations.CreateModel(
            name='OtherEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipmentName', models.CharField(default='Tafel', max_length=10, verbose_name='Sonstige Ausstatung')),
                ('room', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_management.room', verbose_name='Raumname')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_management.location', verbose_name='Raum Ort'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0014_remove_address_building_remove_address_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='ups',
        ),
        migrations.AddField(
            model_name='device',
            name='ups',
            field=models.CharField(default='Имеется', max_length=200),
        ),
    ]

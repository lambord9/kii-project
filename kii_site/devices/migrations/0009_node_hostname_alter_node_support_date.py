# Generated by Django 4.2.7 on 2023-11-27 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_rename_devices_device_rename_nodes_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='hostname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.device'),
        ),
        migrations.AlterField(
            model_name='node',
            name='support_date',
            field=models.DateField(),
        ),
    ]

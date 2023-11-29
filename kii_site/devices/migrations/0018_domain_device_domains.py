# Generated by Django 4.2.7 on 2023-11-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0017_remove_device_ups_node_ups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(default=None, max_length=7, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='domains',
            field=models.ManyToManyField(to='devices.domain'),
        ),
    ]

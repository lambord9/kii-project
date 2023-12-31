# Generated by Django 4.2.7 on 2023-11-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0018_domain_device_domains'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='dev_type',
        ),
        migrations.RemoveField(
            model_name='node',
            name='model',
        ),
        migrations.AddField(
            model_name='device',
            name='dev_type',
            field=models.CharField(choices=[('F', 'Fortigate'), ('К', 'Континент'), ('T', 'Tufin')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

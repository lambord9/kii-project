# Generated by Django 4.2.7 on 2023-11-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_device_mrf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrf', models.CharField(blank=True, choices=[('SZ', 'Северо-запад'), ('DV', 'Дальний восток'), ('VL', 'Волга'), ('SI', 'Сибирь'), ('UG', 'Юг'), ('UR', 'Урал'), ('CN', 'Центр')], max_length=2, null=True)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=7)),
                ('territory_type', models.CharField(max_length=20, null=True)),
                ('contacts', models.CharField(max_length=200)),
                ('ups', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_type', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=15)),
                ('hostname', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('A', 'Active'), ('N', 'Non-active'), ('P', 'Prod')], max_length=1)),
                ('mgmt_inband_ip', models.CharField(max_length=25, null=True)),
                ('mgmt_loopback_ip', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('node', models.CharField(max_length=15)),
                ('serial', models.CharField(max_length=30)),
                ('support_date', models.CharField(max_length=10)),
                ('mgmt_ooband_ip', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]

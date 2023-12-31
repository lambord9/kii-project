# Generated by Django 4.2.7 on 2023-11-29 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0019_remove_node_dev_type_remove_node_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmware', models.CharField(default='6.4', max_length=15)),
                ('build', models.CharField(default='2060', max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='node',
            name='build',
        ),
        migrations.RemoveField(
            model_name='node',
            name='firmware',
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='firmware',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.firmware'),
        ),
    ]

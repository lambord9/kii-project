# Generated by Django 4.2.7 on 2023-12-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='instagram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='telegram',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='vk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_image',
            field=models.ImageField(default='default.png', upload_to='account_images'),
        ),
    ]

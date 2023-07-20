# Generated by Django 4.1.7 on 2023-06-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='summary',
        ),
        migrations.AlterField(
            model_name='info',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
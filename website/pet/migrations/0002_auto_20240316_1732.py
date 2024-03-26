# Generated by Django 2.1.15 on 2024-03-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(default=' ', max_length=400),
        ),
    ]
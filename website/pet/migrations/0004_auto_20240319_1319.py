# Generated by Django 2.1.15 on 2024-03-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
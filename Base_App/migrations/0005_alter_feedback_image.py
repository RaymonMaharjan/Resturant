# Generated by Django 5.1.3 on 2024-11-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0004_offer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='feedback/'),
        ),
    ]

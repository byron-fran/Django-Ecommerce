# Generated by Django 5.0 on 2024-01-25 21:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]

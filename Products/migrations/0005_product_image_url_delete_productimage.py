# Generated by Django 5.0 on 2024-04-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_productimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.FileField(blank=True, upload_to='products/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
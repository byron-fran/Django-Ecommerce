# Generated by Django 5.0.6 on 2024-06-03 21:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='categories/')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'marks',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('descount', models.FloatField()),
                ('image_url', models.FileField(blank=True, upload_to='products/')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
                ('mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.mark')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-stock', '-price'],
            },
        ),
    ]

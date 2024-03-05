# Generated by Django 5.0 on 2023-12-20 17:55

import django.db.models.deletion
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
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=200)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField(default='')),
                ('image', models.ImageField(upload_to='productimg')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subcategory')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20171114_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
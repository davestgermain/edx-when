# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 15:01


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_when', '0002_auto_20190318_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdate',
            name='abs_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdate',
            name='actor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdate',
            name='reason',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdate',
            name='rel_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

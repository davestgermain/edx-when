# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-29 09:56
from __future__ import unicode_literals

import django.db.models.deletion
import opaque_keys.edx.django.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyCourse',
            fields=[
                ('id', opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DummyEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='test_models_app.DummyCourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DummySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(db_index=True, help_text='Date this schedule went into effect')),
                ('enrollment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_models_app.DummyEnrollment')),
            ],
        ),
    ]
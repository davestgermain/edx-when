# Generated by Django 2.2.12 on 2020-05-16 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edx_when', '0007_meta_tweaks'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='contentdate',
            index_together={('course_id', 'location')},
        ),
    ]
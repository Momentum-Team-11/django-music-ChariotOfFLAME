# Generated by Django 4.0.3 on 2022-03-04 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Music',
            new_name='Album',
        ),
    ]

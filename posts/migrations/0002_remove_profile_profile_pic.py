# Generated by Django 3.0 on 2022-03-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
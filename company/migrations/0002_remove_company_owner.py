# Generated by Django 4.1.1 on 2022-09-30 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
    ]

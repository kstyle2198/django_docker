# Generated by Django 4.0.6 on 2022-08-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
    ]
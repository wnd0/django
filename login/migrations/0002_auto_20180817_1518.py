# Generated by Django 2.1 on 2018-08-17 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passwaord',
            new_name='password',
        ),
    ]
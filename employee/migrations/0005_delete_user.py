# Generated by Django 3.0.3 on 2020-03-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
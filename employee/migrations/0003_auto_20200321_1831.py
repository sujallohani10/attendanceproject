# Generated by Django 3.0.3 on 2020-03-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200321_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact_info',
            field=models.CharField(max_length=50),
        ),
    ]

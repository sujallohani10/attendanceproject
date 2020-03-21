# Generated by Django 3.0.3 on 2020-03-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('address', models.TextField()),
                ('birth_date', models.DateField()),
                ('contact_info', models.IntegerField()),
                ('gender', models.TextField()),
                ('profile_photo', models.TextField()),
                ('joined_date', models.DateField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]

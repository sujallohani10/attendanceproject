# Generated by Django 3.0.3 on 2020-03-17 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20200304_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='signin_datetime',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='signout_datetime',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='num_of_hours',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='time_in',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='time_out',
            field=models.TimeField(null=True),
        ),
    ]
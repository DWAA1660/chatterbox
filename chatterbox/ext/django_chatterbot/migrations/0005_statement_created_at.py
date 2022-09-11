# Generated by Django 1.10.1 on 2016-12-29 19:20
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbox', '0004_rename_in_response_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text='The date and time that this statement was created at.'
            ),
        ),
    ]

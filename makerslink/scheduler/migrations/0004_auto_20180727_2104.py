# Generated by Django 2.0.5 on 2018-07-27 19:04

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20180727_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulingcalendar',
            name='service_account',
            field=models.FileField(blank=True, help_text='Upload client_secret json-file', null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/larlin/Projects/MakersLink-Scheduling/pks'), upload_to=''),
        ),
    ]

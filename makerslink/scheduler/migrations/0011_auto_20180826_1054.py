# Generated by Django 2.0.5 on 2018-08-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_eventtemplate_num_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinstance',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Ombokning krävs'), (0, 'Ledigt'), (1, 'Bokat'), (2, 'Inställt')], default=0, help_text='Instance status'),
        ),
    ]

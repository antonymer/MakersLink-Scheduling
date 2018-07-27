# Generated by Django 2.0.5 on 2018-07-27 13:16

from django.db import migrations

def create_testdata(apps, schema_editor):
    SchedulingCalendar = apps.get_model('scheduler', 'SchedulingCalendar')
    EventTemplate = apps.get_model('scheduler', 'EventTemplate')
    SchedulingRule = apps.get_model('scheduler', 'SchedulingRule')
    Event = apps.get_model('scheduler', 'Event')

    calendar = SchedulingCalendar.objects.create(name="Testkalender", google_calendar_id="1234", service_account_username="test", timezone="Europe/Stockholm")
    template = EventTemplate.objects.create(name="Template-Måndag", title="Makermåndag", synchronize=False, calendar=calendar)
    rule = SchedulingRule.objects.create(name="Varje måndag", description="Repeats every monday", frequency="WEEKLY", params="byweekday:MO")
    event = Event.objects.create(name="Måndagar", template=template, start="2018-05-27 13:00:00", end="2018-05-27 16:00:00", rule=rule)

class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_testdata)
    ]
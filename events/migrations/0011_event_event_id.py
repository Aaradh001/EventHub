# Generated by Django 5.0.2 on 2024-05-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_guest_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.CharField(default='EH000116', max_length=150),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.2 on 2024-04-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_requirement_requirementdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='requirement_details',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='RequirementDetails',
        ),
    ]

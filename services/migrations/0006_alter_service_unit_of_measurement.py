# Generated by Django 5.0.2 on 2024-04-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_baseservices_unit_of_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='unit_of_measurement',
            field=models.CharField(choices=[('PERSON_COUNT', 'PERSON_COUNT'), ('SQUARE_FEET', 'SQUARE_FEET')], default='PERSON_COUNT', max_length=100),
        ),
    ]

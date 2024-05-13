# Generated by Django 5.0.2 on 2024-04-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_service_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='unit_of_measurement',
            field=models.CharField(choices=[('Persons Count', 'Persons Count'), ('Count', 'Count'), ('Area(Sq_Ft)', 'Area(Sq_Ft)')], default='PERSON_COUNT', max_length=100),
        ),
    ]

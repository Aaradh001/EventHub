# Generated by Django 5.0.2 on 2024-04-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_remove_service_cost_per_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='service/thumbnail'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-26 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=50)),
                ('unit_of_measurement', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childservice', to='services.service')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue_management', '0002_alter_venue_add_line_1_alter_venue_add_line_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='add_line_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='venue',
            name='add_line_2',
            field=models.TextField(),
        ),
    ]

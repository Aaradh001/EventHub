# Generated by Django 5.0.2 on 2024-04-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vendorprofile_otherservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='registration_method',
            field=models.CharField(choices=[('GOOGLE', 'GOOGLE'), ('NORMAL', 'NORMAL')], default='NORMAL', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

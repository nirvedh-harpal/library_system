# Generated by Django 5.0.6 on 2024-06-06 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compartments', '0005_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compartment',
            name='otp',
        ),
    ]

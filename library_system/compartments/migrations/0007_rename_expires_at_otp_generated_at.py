# Generated by Django 5.0.6 on 2024-06-06 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compartments', '0006_remove_compartment_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='expires_at',
            new_name='generated_at',
        ),
    ]
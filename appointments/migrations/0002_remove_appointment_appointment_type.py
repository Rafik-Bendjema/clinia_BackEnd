# Generated by Django 4.2.8 on 2024-01-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_type',
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_alter_appointment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.CharField(max_length=50),
        ),
    ]

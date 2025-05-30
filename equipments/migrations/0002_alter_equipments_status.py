# Generated by Django 5.2 on 2025-04-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipments",
            name="status",
            field=models.CharField(
                choices=[("connected", "Connected"), ("disconnected", "Disconnected")],
                default="Disconnected",
                max_length=255,
            ),
        ),
    ]

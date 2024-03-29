# Generated by Django 5.0.3 on 2024-03-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ScanResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_address", models.CharField(max_length=100)),
                ("port", models.IntegerField()),
                ("is_open", models.BooleanField(default=False)),
            ],
        ),
    ]

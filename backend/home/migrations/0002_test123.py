# Generated by Django 2.2.28 on 2022-08-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0001_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test123",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("t123", models.BigIntegerField()),
            ],
        ),
    ]

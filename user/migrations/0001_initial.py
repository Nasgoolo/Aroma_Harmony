# Generated by Django 5.0 on 2023-12-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("birthday_date", models.DateField()),
                ("email", models.EmailField(max_length=50)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]

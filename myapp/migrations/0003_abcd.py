# Generated by Django 5.1 on 2024-08-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_abc_mobile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Abcd",
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
                ("name", models.CharField(max_length=50)),
                ("mobile", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
            ],
        ),
    ]

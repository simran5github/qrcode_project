# Generated by Django 5.0 on 2023-12-27 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="qr_model",
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
                ("name", models.CharField(max_length=200)),
                ("code", models.ImageField(blank=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("reviewer_name", models.CharField(max_length=50)),
                ("reviewer_mobile", models.IntegerField()),
                ("reviewer_email", models.EmailField(max_length=254)),
                ("reviewer_profile", models.CharField(max_length=100)),
                ("reviewer_message", models.CharField(max_length=500)),
                ("reviewer_review", models.CharField(max_length=500)),
                ("reviewer_country", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="qr_model_auth",
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
                ("name", models.CharField(max_length=200)),
                ("code", models.ImageField(blank=True, upload_to="qrcodes")),
                ("dob", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

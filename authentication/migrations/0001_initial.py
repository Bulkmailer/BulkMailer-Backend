# Generated by Django 4.1.4 on 2023-01-21 17:39

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewUserResgistration",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255,
                        unique=True,
                        validators=[django.core.validators.EmailValidator()],
                        verbose_name="email address",
                    ),
                ),
                ("name", models.CharField(default=None, max_length=150)),
                (
                    "user_name",
                    models.CharField(
                        blank=True, default=None, max_length=150, null=True, unique=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Others", "Others"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("mobile", models.BigIntegerField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OTP",
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
                (
                    "email",
                    models.EmailField(
                        max_length=255,
                        validators=[django.core.validators.EmailValidator()],
                        verbose_name="email address",
                    ),
                ),
                ("otp", models.CharField(blank=True, max_length=4, null=True)),
                ("time", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_verified", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="GmailAPPModel",
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
                ("email", models.CharField(max_length=200, unique=True)),
                ("app_password", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

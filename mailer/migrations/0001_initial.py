# Generated by Django 4.1.4 on 2023-01-21 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Template",
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
                ("template", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SentMail",
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
                ("_from", models.CharField(max_length=200)),
                ("_group", models.CharField(max_length=200)),
                ("_company", models.CharField(blank=True, max_length=200, null=True)),
                ("_body", models.CharField(blank=True, max_length=200, null=True)),
                ("_subject", models.CharField(max_length=200)),
                ("_template", models.CharField(blank=True, max_length=200, null=True)),
                ("_file", models.FileField(blank=True, null=True, upload_to="media")),
                ("_image", models.ImageField(blank=True, null=True, upload_to="media")),
                ("time", models.DateTimeField(auto_now=True)),
                ("celeryID", models.CharField(blank=True, max_length=200, null=True)),
                ("status", models.CharField(default="Pending", max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SchedulingMail",
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
                ("_from", models.CharField(max_length=200)),
                ("_group", models.CharField(max_length=200)),
                ("_company", models.CharField(blank=True, max_length=200, null=True)),
                ("_body", models.CharField(blank=True, max_length=200, null=True)),
                ("_subject", models.CharField(max_length=200)),
                ("_template", models.CharField(blank=True, max_length=200, null=True)),
                ("_file", models.FileField(blank=True, null=True, upload_to="media")),
                ("_image", models.ImageField(blank=True, null=True, upload_to="media")),
                ("_year", models.IntegerField()),
                ("_month", models.IntegerField()),
                ("_date", models.IntegerField()),
                ("_hour", models.IntegerField()),
                ("_minute", models.IntegerField()),
                ("time", models.DateTimeField(auto_now=True)),
                ("celeryID", models.CharField(blank=True, max_length=200, null=True)),
                ("status", models.CharField(default="PENDING", max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Groups",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group_Details",
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
                ("name", models.CharField(max_length=200, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Others", "Others"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailer.groups",
                    ),
                ),
            ],
        ),
    ]

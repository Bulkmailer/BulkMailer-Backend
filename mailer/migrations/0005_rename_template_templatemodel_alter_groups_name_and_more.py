# Generated by Django 4.1.4 on 2023-03-15 22:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mailer", "0004_alter_group_details_email_alter_group_details_gender"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Template",
            new_name="TemplateModel",
        ),
        migrations.AlterField(
            model_name="groups",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="groups",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
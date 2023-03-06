# Generated by Django 4.1.7 on 2023-03-03 07:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_alter_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="online",
            field=models.ManyToManyField(
                blank=True, related_name="online", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
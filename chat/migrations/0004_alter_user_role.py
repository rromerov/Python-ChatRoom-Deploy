# Generated by Django 4.1.7 on 2023-03-04 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="chat.role"
            ),
        ),
    ]

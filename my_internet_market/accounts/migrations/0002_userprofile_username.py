# Generated by Django 4.2.1 on 2023-08-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="username",
            field=models.CharField(default="user", max_length=40),
        ),
    ]

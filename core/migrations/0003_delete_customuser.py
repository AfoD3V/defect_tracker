# Generated by Django 5.1.3 on 2024-11-28 08:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_customuser_role"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]

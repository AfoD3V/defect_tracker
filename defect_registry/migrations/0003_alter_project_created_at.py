# Generated by Django 5.1.3 on 2024-12-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defect_registry", "0002_attachment_comment_userproject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageutils", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogheader",
            name="dimension_checked",
            field=models.BooleanField(default=False),
        ),
    ]

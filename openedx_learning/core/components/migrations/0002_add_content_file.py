# Generated by Django 4.1 on 2023-02-11 21:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("components", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="file",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="content",
            name="data",
            field=models.BinaryField(max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name="content",
            name="size",
            field=models.PositiveBigIntegerField(
                validators=[django.core.validators.MaxValueValidator(100000)]
            ),
        ),
    ]
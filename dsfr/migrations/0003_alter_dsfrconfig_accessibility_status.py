# Generated by Django 3.2.10 on 2021-12-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsfr", "0002_auto_20211209_1557"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dsfrconfig",
            name="accessibility_status",
            field=models.CharField(
                choices=[
                    ("FULL", "totalement"),
                    ("PART", "partiellement"),
                    ("NOT", "non"),
                ],
                default="NOT",
                max_length=4,
                verbose_name="Statut de conformité de l’accessibilité",
            ),
        ),
    ]

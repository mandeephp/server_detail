# Generated by Django 5.0.7 on 2024-07-25 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ORMS",
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
            ],
        ),
        migrations.CreateModel(
            name="ServerMetric",
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
                ("server", models.CharField(db_column="Server", max_length=50)),
                ("start_time", models.TimeField(db_column="StartTime")),
                ("m2m", models.IntegerField(db_column="M2M")),
                ("realised", models.IntegerField(db_column="Realised")),
                (
                    "cepos",
                    models.DecimalField(
                        blank=True,
                        db_column="CEPOs",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "pepos",
                    models.DecimalField(
                        blank=True,
                        db_column="PEPOs",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "equity",
                    models.DecimalField(
                        blank=True,
                        db_column="Equity",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "fut_pos",
                    models.DecimalField(
                        blank=True,
                        db_column="FutPos",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "total_pos",
                    models.DecimalField(
                        blank=True,
                        db_column="TotalPos",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "delta",
                    models.DecimalField(
                        blank=True,
                        db_column="Delta",
                        decimal_places=3,
                        max_digits=20,
                        null=True,
                    ),
                ),
                (
                    "scripts",
                    models.IntegerField(blank=True, db_column="Scripts", null=True),
                ),
                (
                    "streams",
                    models.IntegerField(blank=True, db_column="Streams", null=True),
                ),
                (
                    "stream_number",
                    models.IntegerField(
                        blank=True, db_column="StreamNumber", null=True
                    ),
                ),
                (
                    "orms",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.orms",
                    ),
                ),
            ],
            options={
                "db_table": "Date21072024",
            },
        ),
    ]

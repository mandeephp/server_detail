# Generated by Django 5.0.7 on 2024-08-15 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_setup_alter_orms_options"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="servermetric",
            table="server_metrics",
        ),
    ]

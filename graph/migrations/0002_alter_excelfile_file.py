# Generated by Django 5.0.1 on 2024-03-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("graph", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="excelfile",
            name="file",
            field=models.FileField(upload_to="graph/static/graph/"),
        ),
    ]
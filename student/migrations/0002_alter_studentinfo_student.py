# Generated by Django 4.2.7 on 2023-11-29 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentinfo",
            name="student",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="student.student"
            ),
        ),
    ]

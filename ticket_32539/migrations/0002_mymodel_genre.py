# Generated by Django 5.0.dev20230121185839 on 2023-02-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket_32539", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mymodel",
            name="genre",
            field=models.CharField(
                choices=[
                    ("ROCK", "Rock"),
                    ("POP", "Pop"),
                    ("JAZZ", "Jazz"),
                    ("CLASSICAL", "Classical"),
                ],
                default="ROCK",
                max_length=10,
            ),
        ),
    ]

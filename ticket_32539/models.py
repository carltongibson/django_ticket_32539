from django.db import models


class GenreChoice(models.TextChoices):
    ROCK = "ROCK", "Rock"
    POP = "POP", "Pop"
    JAZZ = "JAZZ", "Jazz"
    CLASSICAL = "CLASSICAL", "Classical"


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    nr_of_members = models.IntegerField()
    genre = models.CharField(
        max_length=10,
        choices=GenreChoice.choices,
        default=GenreChoice.ROCK,
    )

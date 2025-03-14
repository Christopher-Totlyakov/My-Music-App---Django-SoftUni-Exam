from django.db import models
from albums.choices import GenreChoices
from django.core.validators import MinValueValidator

class Album(models.Model):
    album_name = models.CharField(
        max_length = 30,
        unique = True,
        )

    artist = models.CharField(
        max_length = 30,
        )
    
    genre = models.CharField(
        max_length = 50,
        choices=GenreChoices.choices,
        )

    description = models.TextField(
        blank = True,
        null = True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ]
    )

    owner = models.ForeignKey(
        to = 'profiles.Profile',
        related_name = "albums",
        on_delete = models.CASCADE,
    )
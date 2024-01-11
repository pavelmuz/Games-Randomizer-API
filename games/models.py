import uuid
from django.db import models

# Create your models here.


class Game(models.Model):
    CATEGORIES = (
        ('collection', 'Collection'),
        ('monthly_games', 'Monthly Games'),
        ('coming_monthly_games', 'Coming Monthly Games'),
        ('coming_soon', 'Coming Soon')
    )

    category = models.CharField(choices=CATEGORIES)
    name = models.CharField(max_length=50)
    release = models.DateField()
    expiration = models.DateField(null=True, blank=True)
    platform = models.ManyToManyField('Platform', blank=True)
    genre = models.ManyToManyField('Genre', blank=True)
    russian_audio = models.BooleanField()
    russian_subtitles = models.BooleanField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=20)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.name

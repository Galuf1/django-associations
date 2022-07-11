from concurrent.futures.process import _chain_from_iterable_of_lists
from email import charset
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie, through="Role",related_name="actors")
    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (("actor", "movie"))
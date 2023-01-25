from django.db import models


class Project(models.Model):
    """Project Class."""
    title = models.CharField(max_length=200, unique=True)
    image = models.TextField(unique=True)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    """User Class."""
    pass

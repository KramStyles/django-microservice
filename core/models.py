from django.db import models


class Project(models.Model):
    """Project Class."""
    class Meta:
        app_label = "core"

    title = models.CharField(max_length=200)
    image = models.TextField()
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    """User Class."""
    class Meta:
        """Added this because consumer wasn't seeing its class name."""
        app_label = "core"
    pass

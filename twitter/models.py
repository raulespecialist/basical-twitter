from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    name = models.CharField(max_length=20, blank=False)
    tweet = models.CharField(max_length=50, blank=False)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.name

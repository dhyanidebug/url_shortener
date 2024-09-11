from django.db import models


class urls(models.Model):
    long_url = models.URLField()
    key = models.CharField(primary_key=True, max_length=10)
    short_url = models.URLField()
    impression = models.IntegerField(default=0)

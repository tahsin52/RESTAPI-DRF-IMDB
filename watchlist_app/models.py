from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=55)
    about = models.CharField(max_length=155)
    website = models.URLField(max_length=155)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    title = models.CharField(max_length=155)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



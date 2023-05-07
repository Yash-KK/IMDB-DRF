from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

#MODEL
from accounts.models import (
    CustomUser
)

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class StreamingPlatform(TimeStamp):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Streaming Platform"
        verbose_name_plural = "Streaming Platform's"

    def __str__(self):
        return f"{self.name}"

class WatchList(TimeStamp):
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='watchlist')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    total_reviews = models.IntegerField(default=0)
    avg_ratings = models.FloatField(default=0)

    class Meta:
        verbose_name = "WatchList"
        verbose_name_plural = "WatchList's"
        
    def __str__(self):
        return f"{self.name}"
    
class Review(TimeStamp):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Review's"

    def __str__(self):
        return f"{self.rating}: {self.description} ({self.user.username})"
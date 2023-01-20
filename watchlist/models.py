from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return f"{self.name}: {self.website}"

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    total_reviews = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"   

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"({self.rating}) {self.description} by: {self.user}"
    
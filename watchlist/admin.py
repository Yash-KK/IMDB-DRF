from django.contrib import admin

#MODELS
from .models import (
    Movie,
    StreamingPlatform,
    Review
)
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'description', 'user']
admin.site.register(Movie)
admin.site.register(StreamingPlatform)
admin.site.register(Review, ReviewAdmin)




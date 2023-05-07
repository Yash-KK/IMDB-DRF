from django.contrib import admin

#MODEL
from .models import (
    StreamingPlatform,
    WatchList,
    Review
)
# Register your models here.

class SPlatformAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'active']
    list_display_links = ['name']

class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id','name','total_reviews', 'avg_ratings', 'platform']
    list_display_links = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'watchlist','user']
    list_display_links = ['id', 'rating']

admin.site.register(StreamingPlatform, SPlatformAdmin)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Review, ReviewAdmin)


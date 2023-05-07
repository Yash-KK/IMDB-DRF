from rest_framework import serializers

#MODEL
from .models import (
    StreamingPlatform,
    WatchList,
    Review
)

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Review
        exclude = ['id','watchlist','active','created_at', 'modified_at']

    def get_user(self, obj):
        return obj.user.username
    
class WatchListSerializer(serializers.ModelSerializer):    
    reviews = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        exclude = ['modified_at']

    def validate(self, data):
        name = data['name']
        platform = data['platform']        
        if WatchList.objects.filter(name=name, platform=platform).exists():
            raise serializers.ValidationError(f"{name} already exists!")
        return data
    
    def get_reviews(self, obj):
        serializer = ReviewSerializer(Review.objects.filter(watchlist=obj), many=True)
        return serializer.data

class SPlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.SerializerMethodField()
    class Meta:
        model = StreamingPlatform
        exclude = ['modified_at']
    
    def get_watchlist(self, obj):
        queryset = WatchList.objects.filter(platform=obj)
        serializer = WatchListSerializer(queryset, many=True)        
        data = []
        for watchlist in serializer.data:
            watchlist_data = {
                'name': watchlist['name'],
                'description': watchlist['description'],
                'active': watchlist['active'],
                'total_reviews': watchlist['total_reviews'],
                'average_ratings': watchlist['avg_ratings']
            }
            data.append(watchlist_data)
        return data
    

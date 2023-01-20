from rest_framework import serializers

#MODELS
from .models import (
    Movie,
    StreamingPlatform,
    Review
)

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['movie']        
    
class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)    
    class Meta:
        model = Movie
        fields = '__all__'

class StreamingPlatformSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    # movies = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
        
        


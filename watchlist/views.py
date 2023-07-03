from django.shortcuts import render
from django.http import Http404

#REST FRAMEWORK
from rest_framework.response import Response
from rest_framework import status, generics, serializers
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle

from .permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrReadOnly
)

#SERIALIZER
from .serializer import (
    SPlatformSerializer,
    WatchListSerializer,
    ReviewSerializer
)

#MODEL
from .models import (
    StreamingPlatform,
    WatchList,
    Review
)
# Create your views here.

class SPlatformListAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'platform-list'

    def get(self,request):
        splatforms = StreamingPlatform.objects.filter(active=True)
        serializer = SPlatformSerializer(splatforms, many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = SPlatformSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SplatformDetailAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'platform-detail'

    def get_object(self, pk):
        try:
            return StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        platform = self.get_object(pk)
        serializer = SPlatformSerializer(platform)
        return Response(serializer.data)
    

    def put(self, request, pk):
        platform = self.get_object(pk)
        data = request.data
        serializer = SPlatformSerializer(platform, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        platform = self.get_object(pk)
        platform.delete()
        return Response({
            "info": "instance deleted"
        }, status=status.HTTP_204_NO_CONTENT)
    

class WatchListAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'watchlist'

    def get(self, request):
        watchlists = WatchList.objects.filter(active=True).order_by('created_at')
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = WatchListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchListDetailAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'watch-detail'
    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        watchlist = self.get_object(pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        watchlist = self.get_object(pk)
        data = request.data
        serializer = WatchListSerializer(watchlist, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        watchlist = self.get_object(pk)
        watchlist.delete()
        return Response({
            'info': "instance deleted"
        }, status=status.HTTP_204_NO_CONTENT)

class ReviewCreateAPI(generics.CreateAPIView):
    queryset = Review.objects.filter(active=True)
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        user = self.request.user
        if Review.objects.filter(user=user, watchlist=watchlist).exists():
            raise serializers.ValidationError("User has already reviewed this Movie!")
        
        if watchlist.total_reviews == 0:
            watchlist.total_reviews = 1 
            watchlist.avg_ratings = serializer.validated_data['rating']
            watchlist.save()            
        else:
            watchlist.total_reviews +=1
            watchlist.avg_ratings = (watchlist.avg_ratings + serializer.validated_data['rating'])/2
            watchlist.save()   

        serializer.save(user=user, watchlist=watchlist)


class ReviewListAPI(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.filter(active=True)
    serializer_class = ReviewSerializer

    def perform_destroy(self, instance):
        watchlist_pk = self.kwargs['movie']
        watchlist = WatchList.objects.get(pk=watchlist_pk)
        
        if watchlist.total_reviews == 1:
            watchlist.avg_ratings = 0
            watchlist.total_reviews = 0      
            watchlist.save()
        else:
            final = ((watchlist.avg_ratings * watchlist.total_reviews) - instance.rating)/(watchlist.total_reviews - 1)
            watchlist.avg_ratings = final
            watchlist.total_reviews -=1
            watchlist.save()
        
        return super().perform_destroy(instance)
    
    def perform_update(self, serializer):
        review_instance = Review.objects.get(pk=self.kwargs['pk'])
        watchlist = WatchList.objects.get(pk=self.kwargs['movie'])

        previous_rating = review_instance.rating
        new_rating = serializer.validated_data['rating']

        if watchlist.total_reviews== 1:
            watchlist.avg_ratings = serializer.validated_data['rating']
            watchlist.save()
        else:
            final = (((watchlist.avg_ratings * watchlist.total_reviews)-previous_rating) + new_rating) / (watchlist.total_reviews)
            watchlist.avg_ratings = final
            watchlist.save()

        return super().perform_update(serializer)


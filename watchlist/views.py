#REST FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import (
    IsOwnerOrReadOnly,
    isAdminorReadOnly
)
from .pagination import MovieListPagination

#DJANGO
from django.http import Http404
#MODELS
from .models import (
    Movie,
    StreamingPlatform,
    Review
)

#SERIALIZERS
from .serializers import (
    MovieSerializer,
    StreamingPlatformSerializer,
    ReviewSerializer
)

# Create your views here.


# Only to test filtering functionality
class AllReviews(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    # Query Parameters
    # def get_queryset(self):
    #     queryset = Review.objects.all()
    #     username = self.request.query_params.get('naam')
    #     if username is not None:
    #         queryset = queryset.filter(user__username=username)
    #     return queryset

# FOR TEST PURPOSES
class MovieListGeneric(generics.ListAPIView):
    pagination_class = MovieListPagination
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(pk=movie_id) 
        
        # raise an error if a review by a user already exists
        review_exists = Review.objects.filter(user=self.request.user, movie=movie).exists()
        if review_exists:
            raise ValidationError("User has already reviewed this movie!")
        
        # total reviews and average rating
        if movie.total_reviews == 0:
            movie.average_rating = serializer.validated_data['rating']
        else:
            movie.average_rating = (movie.average_rating + serializer.validated_data['rating'])/2
        movie.total_reviews = movie.total_reviews + 1
        movie.save()
            
        serializer.save(movie=movie, user=self.request.user)

class ReviewList(generics.ListAPIView):    
    permission_classes =[IsAuthenticated]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
     
    def get_queryset(self):
        movie_id = self.kwargs['pk']
        return Review.objects.filter(movie=movie_id) 
        
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class MovieList(APIView):    
    permission_classes = [isAdminorReadOnly]    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetail(APIView):      
    permission_classes = [isAdminorReadOnly]
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            raise Http404 
        
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = request.data
        movie = self.get_object(pk)
        seiralizer = MovieSerializer(movie, data=data)
        if seiralizer.is_valid():
            seiralizer.save()
            return Response(seiralizer.data)
        else:
            return Response(seiralizer.errors)
    
    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamingPList(APIView):
    permission_classes = [isAdminorReadOnly]
    def get(self, request):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = StreamingPlatformSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class StreamingPDetail(APIView):
    permission_classes = [isAdminorReadOnly]
    def get_object(self, pk):
        try:
            return StreamingPlatform.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        platform = self.get_object(pk)
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)
        
    def put(self, request, pk):
        data = request.data
        platform = self.get_object(pk)
        serializer = StreamingPlatformSerializer(platform, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        
    
    def delete(self, request, pk):
        platform = self.get_object(pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#FUNCTION BASED VIEWS
"""
@api_view(['GET', 'POST'])
def movie_list(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)        
        return Response(serializer.data)

    if request.method == 'POST':
        data =request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)        
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
"""



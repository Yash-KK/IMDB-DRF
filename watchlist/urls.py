from django.urls import path

from .views import (
    MovieList,
    MovieDetail,
    
    StreamingPList,
    StreamingPDetail,
    
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    
    
    # For Filtering 
    AllReviews,
    MovieListGeneric
)

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('list/<int:pk>/', movie_detail, name='movie-detail')
    
    path('list/', MovieList.as_view(), name='movie-list'),
    path('list/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    
    path('stream/', StreamingPList.as_view(), name='stream-list'),
    path("stream/<int:pk>/", StreamingPDetail.as_view(), name='stream-detail'),
    
    path('stream/<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('stream/reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    
    # For testing out filtering functionality
    path('stream/all-reviews/', AllReviews.as_view(), name='all-reviews'),
    path('movies/', MovieListGeneric.as_view(), name='all-movies')
    
]

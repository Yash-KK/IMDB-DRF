from django.urls import path

# VIEWS
from .views import (
    SPlatformListAPI,
    SplatformDetailAPI,

    WatchListAPI,
    WatchListDetailAPI,

    ReviewCreateAPI,
    ReviewListAPI,
    ReviewDetailAPI    

)
urlpatterns = [
    path('platform-list/', SPlatformListAPI.as_view(), name='platform-list'),
    path('platform-list/<int:pk>/', SplatformDetailAPI.as_view(), name='platform-detail'),

    path('watch-list/', WatchListAPI.as_view(), name='watch-list'),
    path('watch-list/<int:pk>/', WatchListDetailAPI.as_view(), name='watch-detail'),

    path('watch-list/<int:pk>/review-create/', ReviewCreateAPI.as_view(), name='review-create'),
    path('watch-list/<int:pk>/reviews/', ReviewListAPI.as_view(),name='review-list'),
    path('watch-list/<int:movie>/review-detail/<int:pk>/', ReviewDetailAPI.as_view(), name='review-detail')
]

from django.urls import path
from rest_framework.authtoken import views

#VIEWS
from .views import (
    register_user,
    logout_user
)
urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('register/', register_user, name='register-user'),
    path('logout/', logout_user, name='logout')
]

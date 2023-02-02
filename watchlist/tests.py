from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from .models import (
    StreamingPlatform,
    Movie,
    Review
)

# Create your tests here.
class PlatformTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='secreTT@')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamingPlatform.objects.create(
            name='Netflix',
            description = "#1 Platform",
            website = 'https://www.netflix.com'
        )
    #Normal User ->  Forbidden
    def test_create(self):
        url = reverse('stream-list')
        data = {
            'name': "Hotstar",
            'description': "Just Hotstar!",
            'website': "https://www.hotstar.com"
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    # Normal User
    def test_get_list(self):
        url = reverse('stream-list')
        response = self.client.get(url)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Normal User
    def test_get_individual(self):
        url = reverse('stream-detail', args=(self.stream.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
class MovieTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='secreTT@')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamingPlatform.objects.create(
            name='Hotstar',
            description ='#1 Platform',
            website='https://www.hotstar.com'
        )
        
        self.movie = Movie.objects.create(
            title= "Test Movie",
            description= "Testing",
            platform= self.stream,
            active=True  
        )
        
    # Normal User -> Forbidden
    def test_create(self):
        data = {
            'title': "Test Movie",
            'description': "Testing",
            'platform': self.stream.pk,
            'active':True            
        }
        url = reverse('movie-list')        
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_get_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_individual(self):
        url = reverse('movie-detail', args=(self.movie.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='secreTT@')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamingPlatform.objects.create(
            name='Hotstar',
            description ='#1 Platform',
            website='https://www.hotstar.com'
        )
        
        self.movie = Movie.objects.create(
            title= "Test Movie",
            description= "Testing",
            platform= self.stream,
            active=True  
        )
        self.movie2 = Movie.objects.create(
            title= "Test Movie2",
            description= "Testing2",
            platform= self.stream,
            active=True  
        )
        self.review = Review.objects.create(
            user= self.user,
            movie=self.movie2,
            rating=5,
            description = "Test Review2"
        )
         
    
    def test_create_authorized(self):
        data = {
            'user': self.user.pk,
            'movie': self.movie.pk,
            'rating': 5,
            'description': "Test Review"
        }
        url = reverse('review-create', args=(self.movie.pk,))
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        data = {
            'user': self.user.pk,
            'movie': self.movie2.pk,
            'rating': 2,
            'description': "Test Review",
            'active': False
        }
        
        url = reverse('review-detail', args=(self.review.pk,))
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

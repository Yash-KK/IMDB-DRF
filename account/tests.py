from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.

class RegistrationTest(APITestCase):
    
    def test_regisration(self):
        data = {
            'username': "namefirst",
            'email': 'username@gmail.com',
            'password': 'secreTT@',
            'confirm_password': 'secreTT@'
        }   
        
        url = reverse('register')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.first().username, 'namefirst')
     

class LoginTest(APITestCase):    
    def setUp(self):
        self.user = User.objects.create_user(username='firstname', password='secreTT@')
        self.token = Token.objects.create(user=self.user)       
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    def test_login(self):
        data = {
            'username': 'firstname',
            'password': 'secreTT@'
        }
        url = reverse('login')
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
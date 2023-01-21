from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):        
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords must match.")       
        
        email = data['email']
        if email and User.objects.filter(email=email).exists():
                raise serializers.ValidationError("A user with that email address already exists.")
        return data
        
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
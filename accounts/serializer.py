from rest_framework import serializers

#MODEL
from .models import (
    CustomUser
)

class CustomUserSerializer(serializers.ModelSerializer):   
    confirm_password = serializers.CharField(write_only=True) 
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender','email', 'username', 'password', 'confirm_password']
    
    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']
        email = data['email']
        if password != confirm_password:
            raise serializers.ValidationError("Password's do not match!")

        if CustomUser.objects.filter(email = email).exists():
            raise serializers.ValidationError("User with email already exists!")        
        return data
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        email = validated_data['email']
        gender = validated_data['gender']

        password = validated_data['password']

        user = CustomUser.objects.create(first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         username=username,
                                         gender=gender
                                        )
        user.set_password(password)
        user.save()
        return user
    

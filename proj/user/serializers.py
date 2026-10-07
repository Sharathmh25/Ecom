from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.authentication import RefreshToken
class RegisterSerialer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,blank=False)
    class Meta:
        model=User
        fields=['name','email','password']
        def validate_user(self,value):
            if User.objects.filter(email='email').exists():
                raise serializers.ValidationError("user already exists")
            return value
        def validate_user(self,validate_data):
            User.objects.create_user(**validate_data)
            return User
 
        
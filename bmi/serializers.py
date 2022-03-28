from rest_framework import serializers
from .models import * 


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = bmiapi
        fields = '__all__'


# class GetUserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = '__all__'
#         depth = 2

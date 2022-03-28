from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
class UserList(APIView):
    """
    List all Users, or create a new User object.
    """
    #permission_classes = [IsAllowedToWrite]
    def get(self, request, format=None):
        task = bmiapi.objects.all()
        serializer = UserSerializer(task, many=True)
        return Response(serializer.data)
    #@csrf_exempt
    def post(self, request):
        #height = height/100
        # weight/(height)
        # serializer = UserSerializer(data = request.data)
        # Name = request.data.get('Name')
        # Gender = request.data.get('Gender')
        # HeightCm = request.data.get('HeightCm')
        # WeightKg = request.data.get('WeightKg')
        data = request.data
        response = []
        count = 0
        for person in data:
            height = person["HeightCm"]/100
            bmi = person["WeightKg"]/(height)
            if bmi <= 18.4:
                response.append({"Name": person["Name"], "BMI Category": "Underweight", "Health risk": "Malnutrition risk"})
            elif bmi >= 18.5 and bmi<=24.9: 
                response.append({"Name": person["Name"], "BMI Category": "Normal weight", "Health risk": "Low risk"})
            elif bmi >= 25 and bmi<=29.9:
                response.append({"Name": person["Name"], "BMI Category": "Overweight", "Health risk": "Enhanced risk"}) 
                count += 1 
            elif bmi >= 30 and bmi<=34.9:
                response.append({"Name": person["Name"], "BMI Category": "Moderately obese", "Health risk": "Medium risk"})
            elif bmi >= 35 and bmi<=39.9:
                response.append({"Name": person["Name"], "BMI Category": "Severely obese", "Health risk": "High risk"})
            elif bmi >= 40:
                response.append({"Name": person["Name"], "BMI Category": "Very severely obese", "Health risk": "Very high risk"})
                
        return Response({
            "Count of Overweight": count,
            "Observation":response
        })

        # return Response(serializer.data, status=status.HTTP_201_CREATED)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccoutsSerializer,MyTokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
User=get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegstrationUser(APIView):
  
  def post(self, request):
    serilizer= AccoutsSerializer(data=request.data)
    if serilizer.is_valid():
      serilizer.save()
      return Response(serilizer.data,status=status.HTTP_201_CREATED)
    else:
      return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    
      
    
class RetriveUsers(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request,):
    users=User.objects.all()
    serilizer= AccoutsSerializer(users,many=True)
    return Response(serilizer.data,status=status.HTTP_200_OK)
  
    
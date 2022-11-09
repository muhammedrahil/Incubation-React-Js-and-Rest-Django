from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User=get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class AccoutsSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields = [ 'email', 'password','phone_no','first_name','last_name','Company','Company_url']
    # extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
      user = super().create(validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user

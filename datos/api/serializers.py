from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import CustomUser,post


class UserSerializer(serializers.ModelSerializer):
  class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name','last_name','telefono','edad','ubicacion','email']

class PubliSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

    
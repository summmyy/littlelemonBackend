from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking, Employees

class UserSerializer(serializers.ModelSerializer):
    class Meta:
     model = User
     fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
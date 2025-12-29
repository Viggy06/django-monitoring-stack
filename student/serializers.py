from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'city']

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ['id', 'email']
        fields = ['id', 'name', 'age', 'email', 'city']
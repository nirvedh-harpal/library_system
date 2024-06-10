# compartments/serializers.py
from rest_framework import serializers
from .models import Compartment

class CompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartment
        fields = '__all__'

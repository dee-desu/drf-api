
from rest_framework import serializers
from .models import Dee
class DeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dee
       # fields=['id','name','owner', 'description']
        fields= '__all__'

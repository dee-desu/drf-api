from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import DeeSerializer
# Create your views here. 
from .models import Dee
class DeeListView(ListCreateAPIView):
    queryset=Dee.objects.all()
    serializer_class= DeeSerializer
    

class DeeDetailView (RetrieveUpdateDestroyAPIView):
    queryset=Dee.objects.all()
    serializer_class= DeeSerializer
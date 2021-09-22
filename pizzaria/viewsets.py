from pizzaria import serializers
from django.shortcuts import render
from .models import Cliente
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PizzariasView(ListCreateAPIView):
    serializer_class = serializers.PizzariaSerializer
    queryset = Cliente.objects.all()
    
    
class PizzariaView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PizzariaSerializer
    queryset = Cliente.objects.all()


from rest_framework import serializers
from pizzaria import models

class PizzariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'
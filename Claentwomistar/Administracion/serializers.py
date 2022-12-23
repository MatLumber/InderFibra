from rest_framework import serializers
from Administracion.models import Productos


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

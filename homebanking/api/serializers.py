from rest_framework import serializers
from .models import Sucursal
from .models import Movimientos

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        # indicamos que use todos los campos
        fields = "__all__"
        # les decimos cuales son los de solo lectura
        
        
class MovimientosSerializer(serializers.ModelSerializer):
     class Meta:
        model = Movimientos
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

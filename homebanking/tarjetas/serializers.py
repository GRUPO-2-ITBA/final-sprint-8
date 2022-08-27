from rest_framework import serializers
from .models import Tarjeta


class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"

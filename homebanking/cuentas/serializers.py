from rest_framework import serializers
from .models import Cuenta


class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"

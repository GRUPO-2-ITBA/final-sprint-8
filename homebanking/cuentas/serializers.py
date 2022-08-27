from rest_framework import serializers
from .models import Cuenta, TipoCuenta
from django.db import models


class CuentasSerializer(serializers.ModelSerializer):
    account_type = serializers.IntegerField(source="account_type_id")

    class Meta:
        model = Cuenta
        fields = ("balance", "iban", "account_type")

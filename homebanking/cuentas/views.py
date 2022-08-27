from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from api.permissions import esEmpleado
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Empleado
from .models import Cuenta
from clientes.models import Cliente
from .serializers import CuentasSerializer


@login_required
def cuentas(request):
    return render(request, "cuentas/cuentas.html")


class CuentaCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cliente_dni):
        user = request.user
        owner = str(cliente_dni)
        cliente = Cliente.objects.filter(customer_dni=owner).first()
        if (cliente is not None) and (user.username == owner):
            tarjetas = Cuenta.objects.filter(
                customer_id=cliente.customer)
            serializer = CuentasSerializer(tarjetas, many=True)
            if tarjetas:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('no tiene tarjetas este dni', status=status.HTTP_404_NOT_FOUND)
        elif Empleado.objects.filter(employee_dni=user.username) is not None and cliente is not None:
            tarjetas = Cuenta.objects.filter(
                customer_id=cliente.customer)
            serializer = CuentasSerializer(tarjetas, many=True)
            if tarjetas:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('no tiene tarjetas este id', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('no coincide el dni ni es empleado', status=status.HTTP_401_UNAUTHORIZED)

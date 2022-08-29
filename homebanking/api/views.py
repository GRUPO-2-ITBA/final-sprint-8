from .serializers import MovimientosSerializer
from .models import Movimientos
from django.shortcuts import render
# importamos modelo y serializador

from .serializers import SucursalesSerializer
from .models import Sucursal
from .models import Direcciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from clientes.models import Cliente
from .serializers import DireccionesSerializer
from api.models import Empleado
from api.permissions import esEmpleado
from rest_framework import permissions
# Creamos las vistas aca.


class SucursalesLists(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class MovimientosLists(APIView):
    def post(self, request):
        data = request.data
        data['create_at'] = date.today().strftime('%Y-%m-%d')
        serializer = MovimientosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class DireccionCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    

    def put(self, request, cliente_id):
        user = request.user
        owner = str(cliente_id)
        cliente = Cliente.objects.filter(customer_dni=owner).first()
        if (cliente is not None) and ((user.username == owner) or Empleado.objects.filter(employee_dni=user.username) is not None):
            id_direccion = Cliente.objects.get(customer_dni=owner).address_id
            Direccion = Direcciones.objects.filter(
                address_id=id_direccion).first()
            serializer = DireccionesSerializer(Direccion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('Datos mal ingresados', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('no coincide el dni ni es empleado', status=status.HTTP_401_UNAUTHORIZED)

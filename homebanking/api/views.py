from .serializers import MovimientosSerializer
from .models import Movimientos
from django.shortcuts import render
# importamos serializador y modelo

from .serializers import SucursalesSerializer
from .models import Sucursal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
# Create your views here.


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

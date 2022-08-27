from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
# el form del registro
from .forms import RegistroForm
# para crear usuarios
from django.contrib.auth.models import User
# Create your views here.
from api.permissions import esEmpleado
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Empleado
from .models import Cliente
from .serializers import ClientesSerializer

from django.contrib.auth.decorators import login_required


@login_required
def clientes(request):
    return render(request, "clientes/clientes.html")


@login_required
def home(request):
    if request.user.username:
        return render(request, "clientes/home.html", {'name': request.user.username})
    else:
        return render(request, "clientes/home.html")


def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":

        registro_form = registro_form(data=request.POST)

        if registro_form.is_valid():
            cliente_id = request.POST.get('cliente_id', '')
            email = request.POST.get('email', '')
            pwd = request.POST.get('pwd', '')
            user = User.objects.create_user(cliente_id, email, pwd)
            user.save()

            return redirect(reverse('login'))
    return render(request, "clientes/registro.html", {'form': registro_form})


class ClientesData(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cliente_dni):
        user = request.user
        owner = str(cliente_dni)
        cliente = Cliente.objects.filter(customer_dni=owner).first()
        if (cliente is not None) and (user.username == owner):
            cliente = Cliente.objects.filter(customer_dni=owner)
            print(Cliente.objects.filter(customer_dni=owner).first().customer_dni)
            serializer = ClientesSerializer(cliente, many=True)
            if cliente:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('no existe cliente para este dni', status=status.HTTP_404_NOT_FOUND)
        elif Empleado.objects.filter(employee_dni=user.username) is not None and cliente is not None:
            cliente = Cliente.objects.filter(customer_dni=owner)
            serializer = ClientesSerializer(cliente, many=True)
            if cliente:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('no existe cliente para este dni', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('no coincide el dni ni es empleado', status=status.HTTP_401_UNAUTHORIZED)

from datetime import date
from .serializers import PrestamosSerializer
from django.shortcuts import render, redirect
from .forms import PrestamoForm
from .models import Prestamo
from clientes.models import Cliente
from django.contrib.auth.decorators import login_required
from api.permissions import esEmpleado
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Empleado
from cuentas.models import Cuenta


@login_required
def prestamos(request):
    prestamo_form = PrestamoForm
    user = request.user
    cliente = Cliente.objects.get(customer_dni=str(user.username))
    # validamos que ocurrio una peticion POST
    if request.method == "POST":
        # Traemos los datos enviados
        prestamo_form = prestamo_form(data=request.POST)
        print(prestamo_form)
        # Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if prestamo_form.is_valid():
            loan_paymentReceived = request.POST.get('loan_payment', '')
            loan_dateReceived = request.POST.get('loan_date', '')
            loan_totalReceived = request.POST.get('loan_total', '')

            prestamo = Prestamo(loan_payment=loan_paymentReceived, loan_date=loan_dateReceived,
                                loan_total=loan_totalReceived, customer_id=int(cliente.customer))

            cuenta = Cuenta.objects.get(customer_id=int(cliente.customer))
            if cuenta:
                cuenta.balance = int(loan_totalReceived) + cuenta.balance
                cuenta.save()
            prestamo.save()
            return render(request, 'prestamos/prestamos.html', {'enviado': cliente.customer_dni})
    return render(request, 'prestamos/prestamos.html', {'form': prestamo_form})


class PrestamosListCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cliente_id):
        # podemos chequear que un cliente solo haga GET para sus propios prestamos
        user = request.user
        owner = str(cliente_id)
        cliente = Cliente.objects.filter(customer_dni=owner).first()
        if (cliente is not None) and ((user.username == owner) or Empleado.objects.filter(employee_dni=user.username) is not None):
            prestamos = Prestamo.objects.filter(
                customer_id=cliente.customer)
            serializer = PrestamosSerializer(prestamos, many=True)
            if prestamos:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('no tiene prestamos este id', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('no coincide el dni ni es empleado', status=status.HTTP_401_UNAUTHORIZED)


class PrestamosListSucursal(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def get(self, request, sucursal_id):
        clientes = Cliente.objects.filter(branch_id=sucursal_id)
        prestamos = []
        for cliente in clientes:
            if Prestamo.objects.filter(customer_id=cliente.customer).exists():
                prestamos.extend(
                    list(Prestamo.objects.filter(customer_id=cliente.customer)))
        if prestamos:
            serializer = PrestamosSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No hay prestamos asociados a la sucursal', status=status.HTTP_404_NOT_FOUND)


class PrestamosAdd(APIView):
    permission_classes = [esEmpleado]

    def post(self, request):
        data = request.data
        data['loan_date'] = date.today().strftime('%Y-%m-%d')
        serializer = PrestamosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cuenta = Cuenta.objects.get(
                customer_id=request.data["customer_id"])
            if cuenta:
                cuenta.balance = request.data["loan_total"] + cuenta.balance
                cuenta.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("la informacion ingresada no es valida", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, prestamo_id):
        prestamo = Prestamo.objects.filter(loan_id=prestamo_id).first()
        print(prestamo)
        if prestamo:
            serializer = PrestamosSerializer(prestamo)
            cuenta = Cuenta.objects.get(
                customer_id=serializer.data["customer_id"])
            if cuenta:
                cuenta.balance = serializer.data["loan_total"] + cuenta.balance
                cuenta.save()
            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("No existe el prestamo", status=status.HTTP_400_BAD_REQUEST)

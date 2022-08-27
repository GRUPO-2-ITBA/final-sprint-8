from rest_framework import permissions
from clientes.models import Cliente
from .models import Empleado


class esEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        return list(Empleado.objects.filter(employee_dni=username)) != []

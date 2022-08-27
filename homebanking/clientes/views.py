from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
# el form del registro
from .forms import RegistroForm
# para crear usuarios
from django.contrib.auth.models import User
# Create your views here.

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

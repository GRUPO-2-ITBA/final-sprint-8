"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from cuentas import views as views_cuentas
from tarjetas import views as views_tarjetas
from login import views as views_login
from prestamos import views as views_prestamos
from clientes import views as views_clientes
from api import views as views_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_clientes.home, name="home"),
    path('clientes/', views_clientes.clientes, name="clientes"),
    path('prestamos/', views_prestamos.prestamos, name="prestamos"),
    path('tarjetas/', views_tarjetas.tarjetas, name="tarjetas"),
    path('login/', views_login.login, name="login"),
    path('cuentas/', views_cuentas.cuentas, name="cuentas"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro', views_clientes.registro, name="registro"),
    path('api/sucursales/', views_api.SucursalesLists.as_view(),
         name='api_sucursales'),
    path('api/movimientos/', views_api.MovimientosLists.as_view(),
         name='api_movimientos'),
    path('api/prestamos/<int:cliente_id>/',
         views_prestamos.PrestamosListCliente.as_view(), name='api_prestamos_list'),
    path('api/prestamos_sucursal/<int:sucursal_id>/',
         views_prestamos.PrestamosListSucursal.as_view(), name='api_prestamos_sucursal'),
    path('api/tarjetas/<int:cliente_dni>/',
         views_tarjetas.TarjetasListCliente.as_view(), name='api_tarjetas_list'),
    path('api/cliente/<int:cliente_dni>/',
         views_clientes.ClientesData.as_view(), name='api_cliente_data'),
    path('api/cuenta/<int:cliente_dni>/',
         views_cuentas.CuentaCliente.as_view(), name='api_cliente_cuentas'),
    path('api/add_prestamo/',
         views_prestamos.PrestamosAdd.as_view(), name='api_prestamos_add'),
    path('api/delete_prestamo/<int:prestamo_id>/',
         views_prestamos.PrestamosAdd.as_view(), name='api_prestamos_delete'),
    path('api/direcciones/<int:cliente_id>/',
         views_api.DireccionCliente.as_view(), name='api_direccion_update'),
]

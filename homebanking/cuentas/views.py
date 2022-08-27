from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def cuentas(request):
    return render(request, "cuentas/cuentas.html")

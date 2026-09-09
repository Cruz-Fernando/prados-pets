from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    context = {
        "es_administrador": request.user.es_administrador,
    }
    return render(request, "usuarios/dashboard.html", context)

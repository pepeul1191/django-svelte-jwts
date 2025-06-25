from django.shortcuts import render
from .settings import ENV

def home_view(request):
  # Puedes pasar cualquier dato que necesites al template
  context = {
    'mensaje': '¡Bienvenido a mi sitio Django!',
    'nombre_usuario': 'Visitante' # Esto podría venir de la sesión del usuario, etc.
  }
  return render(request, 'home.html', context)
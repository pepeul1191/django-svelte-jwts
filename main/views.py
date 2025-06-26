from django.shortcuts import render
from .settings import ENV

def custom_404(request, exception):
  context = {'path': request.path, 'exception': exception}
  return render(request, '404.html', context, status=404)

def home(request):
  # Puedes pasar cualquier dato que necesites al template
  context = {}
  return render(request, 'home.html', context)

def access(request):
  # Puedes pasar cualquier dato que necesites al template
  context = {}
  return render(request, 'access.html', context)
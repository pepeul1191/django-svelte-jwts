from functools import wraps
from django.shortcuts import redirect

class ServerHeaderMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    response['Server'] = 'Ubuntu'
    return response
  
def login_required(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    # Verifica si 'user' está en la sesión
    if request.session.get('user') is None:
      return redirect('/sign-in?error=Debe estar logueado')  # Cambia por tu URL de login
    return view_func(request, *args, **kwargs)
  return _wrapped_view

def logued_go_home(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    # Verifica si 'user' está en la sesión
    if request.session.get('user') is not None:
      return redirect('/')  # Cambia por tu URL de login
    return view_func(request, *args, **kwargs)
  return _wrapped_view
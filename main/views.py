from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .filters import login_required, logued_go_home

def custom_404(request, exception):
  if request.method == 'GET':
    context = {}
    return render(request, '404.html', context, status=404)
  else:
    response_data = {
      'message': 'Método no permitido',
      'method': request.method,
      'path': request.path,
      'error': ['GET'],
      'status': 405
    }
    return JsonResponse(response_data, status=405)

@login_required
@ensure_csrf_cookie
@require_http_methods(["GET"])
def home(request, _id = 'E'):
  context = {}
  return render(request, 'home.html', context)

@logued_go_home
@ensure_csrf_cookie
@require_http_methods(["GET"])
def access(request):
  context = {}
  return render(request, 'access.html', context)

def signout(request):
  request.session.flush()
  return HttpResponseRedirect('/sign-in')
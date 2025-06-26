from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

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

@ensure_csrf_cookie
@require_http_methods(["GET"])
def home(request):
  context = {}
  return render(request, 'home.html', context)

@ensure_csrf_cookie
@require_http_methods(["GET"])
def access(request):
  context = {}
  return render(request, 'access.html', context)
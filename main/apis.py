from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime
from .helpers import login
import json

@require_http_methods(['POST'])
def user_sign_in(request):
  # Recibir datos del formulario
  data = json.loads(request.body)
  username = data.get('username')
  password = data.get('password')
  if username != '' and password != '':
    answer = login(username, password)
  else:
    answer = {
      'body': {
        'error': 'Debe de ingresar su usuario y contraseña',
        'message': 'Sin el campo de usuario y contraseña no se puede continuar'
      },
      'status': 400
    }
  if answer['status'] == 200:
    request.session['user'] = answer['body']
    request.session['login_at'] = datetime.now().isoformat()  
  return JsonResponse(
    answer['body'],
    status=answer['status']
  )

@require_http_methods(['GET'])
def user_session(request):
  user = request.session.get('user')
  if user:
    login_time = request.session.get('login_at')
    return JsonResponse({
      'user': user,
      'login_at': login_time
    }, status=200)
  else:
    return JsonResponse({
      'error': 'No hay sesión activa',
      'message': 'request.session.get(''user'') = None'
    }, status=401)

@require_http_methods(['POST'])
def user_sign_in2(request):
  return ':)'
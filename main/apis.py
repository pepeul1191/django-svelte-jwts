from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
import json

@require_http_methods(["POST"])
def user_sign_in(request):
  try:
    # Recibir datos del formulario
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
    # Primera petición a la API de autenticación
    access_response = requests.post(
      'http://localhost:8080/api/v1/sign-in',
      json={
        'username': username,
        'password': password,
        'system_id': 1
      },
      headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    )
    
    # Segunda petición al servidor de archivos
    file_response = requests.post(
      'http://localhost:8090/api/v1/sign-in',
      json={},
      headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Trigger': 'dXNlci1zdGlja3lfc2VjcmV0XzEyMzQ1Njc'
      }
    )
    
    # Procesar respuestas
    response_data = access_response.json()
    file_data = file_response.json()
    
    # Agregar token del servidor de archivos a la respuesta
    response_data['file_token'] = file_data.get('token')
    response_data['message'] = 'Login OK'
    
    return JsonResponse(response_data, status=access_response.status_code)
    
  except requests.exceptions.RequestException as e:
    # Manejar errores de conexión
    return JsonResponse(
        {'error': 'No se pudo conectar con la API externa', 'message': str(e)},
        status=503
    )
  except json.JSONDecodeError as e:
    # Manejar errores de JSON
    return JsonResponse(
        {'error': 'Error procesando la respuesta', 'message': str(e)},
        status=500
    )

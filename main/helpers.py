from django import template
from .settings import ENV
import requests
import json

register = template.Library()

@register.simple_tag
def load_env():
  return ENV

def login(username, password):
  answer = {'body': {}, 'status': 200}
  try:  
    # petición a la API de autenticación
    access_response = requests.post(
      ENV['URL_ACCESS_SERVICE'] + 'api/v1/sign-in',
      json={
        'username': username,
        'password': password,
        'system_id': 1
      },
      headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Trigger': ENV['X_AUTH_ACCESS_SERVICE']
      }
    )
    if access_response.status_code == 200:
      tmp = json.loads(access_response.text)
      answer['body']['id'] = tmp['id']
      answer['body']['username'] = tmp['username']
      answer['body']['access_token'] = tmp['token']
      answer['body']['email'] = tmp['email']
      # petición a la API de files
      files_response = requests.post(
        ENV['URL_FILES_SERVICE'] + 'api/v1/auth/generate-token',
        json={
          'user': {
            'id': answer['body']['id'],
            'username': answer['body']['username'],
            'email':answer['body']['email'],
          }
        },
        headers={
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Auth-Trigger': ENV['X_AUTH_FILES_SERVICE']
        }
      )
      # petición a la API de tickets
      tickets_response = requests.post(
        ENV['URL_TICKETS_SERVICE'] + 'api/v1/auth/generate-token',
        json={
          'user': {
            'id': answer['body']['id'],
            'username': answer['body']['username'],
            'email':answer['body']['email'],
          }
        },
        headers={
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Auth-Trigger': ENV['X_AUTH_TICKETS_SERVICE']
        }
      )
      # juntar respuestas de servicios
      if files_response.status_code == 200 and tickets_response.status_code == 200:
        tmp1 = json.loads(files_response.text)
        tmp2 = json.loads(tickets_response.text)
        answer['body']['files_token'] = tmp1['token']
        answer['body']['tickets_token'] = tmp2['token']
      else:
        tmp = tmp1['message'] + ', ' + tmp2['message']
        answer = {
          'body': {
            'error': tmp,
            'message': 'Error al autenticarse con los servicios'
          },
          'status': files_response.status_code
        }
    else:
      tmp = json.loads(access_response.text)
      answer = {
        'body': {
          'error': tmp['message'],
          'message': tmp['error']
        },
        'status': access_response.status_code
      }
  except requests.exceptions.RequestException as e:
    # Manejar errores de conexión
    answer = {
      'body': {
        'error': 'No se pudo conectar con la API externa',
        'message': str(e)
      },
      'status': 503
    }
  except Exception as e:
    # Manejar otros errores
    answer = {
      'body': {
        'error': 'Ocurrió un error al generar los JWTs',
        'message': str(e) 
      },
      'status': 500
    }
  return answer
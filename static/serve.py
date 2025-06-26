  #!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
  """Handler que añade headers CORS a las respuestas"""

  def end_headers(self):
    # Headers para habilitar CORS
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    super().end_headers()

  def do_OPTIONS(self):
    # Responder al preflight request
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', 'http://localhost:8000')
    self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
    self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    self.send_header('Access-Control-Allow-Credentials', 'true')
    self.end_headers()

def run_server(port=8001):
  """Inicia el servidor HTTP con CORS habilitado"""
  server_address = ('', port)
  httpd = HTTPServer(server_address, CORSRequestHandler)
  print(f'Servidor con CORS en http://localhost:{port}')
  httpd.serve_forever()

if __name__ == '__main__':
  run_server()
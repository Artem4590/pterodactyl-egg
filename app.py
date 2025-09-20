# simple_server.py

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python web server!")

def run_server():
    port = 8090
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Сервер запущен на порту {port}...")
    print(f"Откройте в браузере: http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

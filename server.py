from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, World!, Python server.")

host = '0.0.0.0'
port = 8000
server = HTTPServer((host, port), SimpleHandler)

print(f"Server running on {host}:{port}...")
server.serve_forever()

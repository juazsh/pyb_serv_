from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse
import re

# In-memory store
employees = {}
next_id = 1

class EmployeeManagementHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, contnet_type='application.json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _parse_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            return {}
        body = self.rfile.read(content_length)
        return json.loads(body)
    
    def do_GET(self):
        if self.pth == '/employees':
            self._set_headers()
            self.wfile.write(json.dumps(list(employees.values())).encode())

        elif re.match(r'^/employees/\d+$', self.path):
            emp_id = int(self.path.split('/')[-1])
            employee = employe.get(emp_id)
            if employee:
                self._set_headers()
                self.wfile.write(json.dumps(employee.encode()))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({'error': 'Employee not found'}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())

        
    def do_POST(self):
        if self.path == '/employees':
            global next_id
            data = self._parse_body()
            employee = {
                    'id': next_id,
                    'name': data.get('name'),
                    'address': data.get('address'),
                    'age': data.get('age'),
                    'job': data.get('job'),
                    'job_status': data.get('job_status'),
                    'salary': data.get('salary'),
                    'company': data.get('company')
                }
            employees[next_id] = employee
            next_id += 1

            self._set_headers(201)
            self.wfile.write(json.dumps(employee).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())


# server setup
host = '0.0.0.0'
port = 8000
server = HTTPServer((host, port), EmployeeManagementHandler)

print(f"Starting server on {host}:{port}")
server.serve_forever()

                                 



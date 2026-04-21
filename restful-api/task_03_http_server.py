#!/usr/bin/python3
"""
Simple API built using Python's built-in http.server module.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handler for HTTP requests."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            # Əsas səhifə üçün mətn cavabı
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # /data endpointi üçün JSON cavabı
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # /status endpointi üçün sadə OK cavabı
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # /info endpointi üçün JSON cavabı
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Tanınmayan endpointlər üçün 404 xətası
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()

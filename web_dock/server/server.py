import http.server
import socketserver

handle = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 80), handle) as httpd:

    httpd.serve_forever()

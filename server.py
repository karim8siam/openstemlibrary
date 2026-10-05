import http.server
import socketserver
import os
import sys

PORT = 4242
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
        print(f"Server started on http://localhost:{PORT} with zero caching")
        sys.stdout.flush()
        httpd.serve_forever()
except Exception as e:
    print(f"Server error: {e}", file=sys.stderr)
    sys.exit(1)

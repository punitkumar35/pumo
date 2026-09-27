import http.server
import socketserver

PORT = 8910

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    with ThreadedHTTPServer(('0.0.0.0', PORT), NoCacheHandler) as httpd:
        print(f'Serving Y:\PUMO-TEECH on http://localhost:{PORT} (no-cache, threaded)')
        httpd.serve_forever()

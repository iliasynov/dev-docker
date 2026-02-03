from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

HOST = "0.0.0.0"
PORT = int(os.getenv("GAME_PORT", 6000))

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _set_headers(self, code=200, extra=None):
        self.send_response(code)
        self.send_header("Access-Control-Allow-Origin", "*")  # allow browser to connect from frontend
        if extra:
            for k, v in extra.items():
                self.send_header(k, v)
        self.end_headers()

    def do_GET(self):
        if self.path == "/healthz":
            body = b"ok"
            self._set_headers(200, {"Content-Type": "text/plain; charset=utf-8", "Content-Length": str(len(body))})
            self.wfile.write(body)
            return

        if self.path == "/events":
            # SSE stream
            self._set_headers(200, {
                "Content-Type": "text/event-stream; charset=utf-8",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            })

            n = 0
            try:
                # Optional: tell the client reconnect delay (ms)
                self.wfile.write(b"retry: 2000\n\n")
                self.wfile.flush()

                while True:
                    n += 1
                    msg = f"data: {n}\n\n".encode("utf-8")
                    self.wfile.write(msg)
                    self.wfile.flush()
                    time.sleep(2)
            except (BrokenPipeError, ConnectionResetError):
                # client disconnected
                return

        # default
        body = b"Not found"
        self._set_headers(404, {"Content-Type": "text/plain; charset=utf-8", "Content-Length": str(len(body))})
        self.wfile.write(body)

def main():
    print(f"[os server] listening on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()

if __name__ == "__main__":
    main()

"""
Double-click this file to launch your farewell page.
Requires Python 3 (already on most computers).
Keep this file in the SAME folder as index.html, track.mp3, trailer.mp4.
"""

import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    ".mp3": "audio/mpeg",
    ".mp4": "video/mp4",
    ".html": "text/html",
})

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"✓ Server running at http://localhost:{PORT}")
    print("  Opening your browser now...")
    print("  Press Ctrl+C to stop.\n")
    threading.Timer(1.0, open_browser).start()
    httpd.serve_forever()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的HTTP服务器，用于运行3D游戏
"""
import http.server
import socketserver
import os
import sys
import json

# 设置输出编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WATCHED_EXTENSIONS = {
    ".html", ".js", ".css", ".json",
    ".fbx", ".glb", ".gltf",
    ".png", ".jpg", ".jpeg", ".webp", ".gif"
}


def get_content_version():
    latest = 0
    for root, _, files in os.walk(BASE_DIR):
        for filename in files:
            _, ext = os.path.splitext(filename.lower())
            if ext not in WATCHED_EXTENSIONS:
                continue
            full_path = os.path.join(root, filename)
            try:
                mtime_ns = os.stat(full_path).st_mtime_ns
                if mtime_ns > latest:
                    latest = mtime_ns
            except OSError:
                continue
    return latest

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/__hot_reload'):
            version = get_content_version()
            body = json.dumps({"version": version}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store, max-age=0')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        # 添加CORS头，允许加载外部资源
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

os.chdir(BASE_DIR)

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Game Server Started!")
    print(f"Visit: http://localhost:{PORT}")
    print(f"Press Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")

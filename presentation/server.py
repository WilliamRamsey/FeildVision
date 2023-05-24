from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
from numpy import random
import websock
import json
import math

# Address for communicating with browser
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

# Websocket for Communicating with pico
sock = websock.TCPClient("192.168.137.61", 5500).r()
conn = websock.TCPConnection(sock)

class dataServer(BaseHTTPRequestHandler):
    def do_GET(self):
        datalist = []
        while len(datalist) <= 10:
            conn.send("s".encode("utf-8"))
            # Sends the data
            data = conn.receive()
            data = data.replace("'", '"')
            data = json.loads(data)
            magnitude = math.sqrt((data['x'] * data['x']) + (data['y'] * data['y']) + (data['z'] * data['z']))
            datalist.append(magnitude)
        mForce = max(datalist)

        if mForce > 2:
            html = """
<!DOCTYPE html>
<html>
    <head>
        <script>
            setTimeout(function(){location.reload()}, 1000);
        </script>
        <style>
            body {
                background-color: red}
            h1 {font-family: 'Courier New', Courier, monospace;
                color: white;
                text-align: center;
                vertical-align: middle;
            }
        </style>
    </head>
    <body>
        <h1>Maximum impact rating:""" + str(mForce) + """</h1>
        <h1>Concussive impact detected</h1>
    </body>
</html>
"""
        else:
            html = """
<!DOCTYPE html>
<html>
    <head>
        <script>
            setTimeout(function(){location.reload()}, 1000);
        </script>
        <style>
            body {
                background-color: green}
            h1 {font-family: 'Courier New', Courier, monospace;
                color: white;
                text-align: center;
                vertical-align: middle;
            }
        </style>
    </head>
    <body>
        <h1>Maximum impact rating:""" + str(mForce) + """</h1>
        <h1>Non concussive</h1>
    </body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))

server = HTTPServer((HOST, PORT), dataServer)
print(f"Serving on {HOST}:{PORT}")
server.serve_forever()
server.server_close()

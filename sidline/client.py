import websock
import json
# Opens TCP connection
sock = websock.TCPClient("192.168.1.72", 5500).r()
conn = websock.TCPConnection(sock)


while True:
    conn.send("s".encode("utf-8"))
    # Sends the data
    data = conn.receive()
    data = data.replace("'", '"')
    data = json.loads(data)
    print(data)

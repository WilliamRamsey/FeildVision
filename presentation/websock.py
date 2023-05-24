import socket

class TCPServer:
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (HOST, PORT)
        self.s.bind(address)
        self.s.listen()

    def connect_socket(self):
        self.conn, self.addr = self.s.accept()
        return self.conn, self.addr

class TCPClient:
    # Host of server, Port of server
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_adress = (HOST, PORT)
        self.s.connect(self.server_adress)
    
    def r(self):
        return self.s

class TCPConnection:
    def __init__(self, conn):
        self.s = conn
    
    def send(self, data):
        self.s.sendall(data)
    
    def receive(self):
        data = self.s.recv(1024).decode('utf-8')
        return data
    
    def end(self):
        self.s.close()

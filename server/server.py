import serial
import socket
import threading


DISCONNECT = "disconnect"
HEADER = 64
PORT = 8080
SERVER = '0.0.0.0'              #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) 
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    print(f"[server]server is listening... on {ADDR[0]}:{ADDR[1]}")
    while True:
        conn, addr = server.accept()
        
        while True:
            msg = conn.recv(1024)
            print(msg.decode())
            if msg == "stop":
                return

        
print("[server]server is starting...")
start()

server.close()
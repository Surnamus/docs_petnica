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

def handle_client(conn, addr):
    print(addr)
    print(f"[new connection], ,{addr} ,connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg = None
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
        
        if msg is None:
            connect = False #
        print("[{addr}] {msg}")
        conn.send("Message recieved".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[server]server is listening... on {ADDR[0]}:{ADDR[1]}")
    while True:
        conn, addr = server.accept()
        msg = conn.recv(1024).decode(FORMAT)
        print(f"[{addr}] {msg}")
        # thread = threading.Thread(target = handle_client, args = (conn, addr))
        # thread.start()
        print(f"[active], {threading.active_count()- 1}")

print("[server]server is starting...")
start()

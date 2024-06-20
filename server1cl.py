
import socket

HEADER = 64
PORT = 7171
FORMAT = "utf-8"
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "disconnect":
                connected = False
            print(f"[{addr}] {msg}")

    print(f"[DISCONNECTED] {addr} disconnected.")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    conn, addr = server.accept()
    handle_client(conn, addr)

start()

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
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname}left the chat.'.decode('ascii'))
            nicknames.remove(nickname)
            break
def recieve():
    while True:
        conn, addr = server.accept()
        print(f"connected with {str(addr)}")
        conn.send('NICK'.encode('ascii'))
        nickname = conn.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(conn)

        print(f"Your nickname is {nickname}")
        broadcast(f"{nickname} has joined the chat.")
        conn.send('connected to the server'.encode('ascii'))
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
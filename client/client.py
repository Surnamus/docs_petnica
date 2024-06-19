import socket


DISCONNECT = "disconnect"
HEADER = 64
PORT = 8080
FORMAT = "utf-8"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("hello")
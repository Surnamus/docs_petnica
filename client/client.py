import socket


DISCONNECT = "disconnect"
HEADER = 64
PORT = 8080
FORMAT = "utf-8"
SERVER = "192.168.0.137"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

while True:
    msg = input()
    send(msg)

    if msg == "stop":
        break

send("hello")
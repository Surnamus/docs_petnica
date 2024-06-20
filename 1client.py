import socket

HEADER = 64
PORT = 7171
FORMAT = "utf-8"
SERVER = "192.168.0.137" 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR)
except Exception as e:
    print(f"Connection to server failed: {e}")
    exit()

def receive():
    while True:
        try:
            msg_length = client.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = client.recv(msg_length).decode(FORMAT)
                print(msg)
        except Exception as e:
            print(f"Error receiving message: {e}")
            client.close()
            break

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    client.send(send_length)
    client.send(message)

while True:
    message = input("Enter message (type 'disconnect' to quit): ")
    send(message)
    if message == "disconnect":
        break

client.close()

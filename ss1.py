import socket

HEADER = 10  # Fixed length header for message size
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def findpos(cursor_pos, text, character):
    x, y = map(int, cursor_pos.split(','))
    txtarr = text.split("\n")
    txtarr[x] = txtarr[x][:y] + character + txtarr[x][y:]
    return '\n'.join(txtarr)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        with open("text.txt", 'r') as f:
            content = f.read()

        # Send the original text to the client
        content_length = f"{len(content):<{HEADER}}".encode(FORMAT)
        conn.send(content_length)
        conn.send(content.encode(FORMAT))

        cursor_pos = conn.recv(HEADER).decode(FORMAT).strip()
        text = conn.recv(1024).decode(FORMAT)

        modified_content = findpos(cursor_pos, content, text)
        
        # Send the modified text to the client
        modified_content_length = f"{len(modified_content):<{HEADER}}".encode(FORMAT)
        conn.send(modified_content_length)
        conn.send(modified_content.encode(FORMAT))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

print("[STARTING] Server is starting...")
start()

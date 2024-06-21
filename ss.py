'''
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

        cursor_pos = conn.recv(HEADER).decode(FORMAT).strip()
        text = conn.recv(1024).decode(FORMAT)

        modified_content = findpos(cursor_pos, content, text)
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
'''
import socket
import threading
import signal
import sys

HEADER = 10  # Fixed length header for message size
PORT = 8080  # Changed port number to a higher one
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

# Create a socket and set options
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server.bind(ADDR)
except socket.error as e:
    print(f"Socket binding error: {e}")
    sys.exit(1)

def findpos(cursor_pos, text, character):
    try:
        x, y = map(int, cursor_pos.split(','))
        txtarr = text.split("\n")
        if 0 <= x < len(txtarr):
            txtarr[x] = txtarr[x][:y] + character + txtarr[x][y:]
        return '\n'.join(txtarr)
    except Exception as e:
        print(f"Error in findpos function: {e}")
        return text

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        with open("text.txt", 'r') as f:
            content = f.read()

        # Send the original text to the client
        content_length = f"{len(content):<{HEADER}}".encode(FORMAT)
        conn.send(content_length)
        conn.send(content.encode(FORMAT))

        # Receive cursor position
        cursor_pos_length = conn.recv(HEADER).decode(FORMAT).strip()
        if cursor_pos_length:
            cursor_pos = conn.recv(int(cursor_pos_length)).decode(FORMAT)
        else:
            cursor_pos = ""

        # Receive text to insert
        text_to_insert_length = conn.recv(HEADER).decode(FORMAT).strip()
        if text_to_insert_length:
            text_to_insert = conn.recv(int(text_to_insert_length)).decode(FORMAT)
        else:
            text_to_insert = ""

        if cursor_pos and text_to_insert:
            modified_content = findpos(cursor_pos, content, text_to_insert)

            # Send the modified text to the client
            modified_content_length = f"{len(modified_content):<{HEADER}}".encode(FORMAT)
            conn.send(modified_content_length)
            conn.send(modified_content.encode(FORMAT))
            
            # Save the modified content to the file
            with open("text.txt", 'w') as f:
                f.write(modified_content)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except Exception as e:
            print(f"Error accepting connections: {e}")

def signal_handler(sig, frame):
    print('Shutting down server...')
    server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("[STARTING] Server is starting...")
try:
    start()
except Exception as e:
    print(f"Error starting server: {e}")
    server.close()
    sys.exit(1)









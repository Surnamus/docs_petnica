'''
import socket

HEADER = 10
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "192.168.0.110"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def main():
    try:
        cursor_pos = input("Enter the cursor position (row,column): ")
        text_to_insert = input("Enter the text to insert: ")

        cursor_pos = f"{cursor_pos:<{HEADER}}"
        client.send(cursor_pos.encode(FORMAT))
        client.send(text_to_insert.encode(FORMAT))

        modified_text = client.recv(1024).decode(FORMAT)
        print("Modified Text:")
        print(modified_text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.send(DISCONNECT_MESSAGE.encode(FORMAT))
        client.close()

if __name__ == "__main__":
    main()
    '''
'''
import socket
import threading

HEADER = 10
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "192.168.0.137"
ADDR = (SERVER, PORT)

def send_data(client):
    try:
        while True:
            cursor_pos = input("Enter the cursor position or 'disconnect' to exit: ")
            if cursor_pos.lower() == 'disconnect':
                break
            
            text_to_insert = input("Enter the text to insert: ")

            cursor_pos_header = f"{len(cursor_pos):<{HEADER}}"
            client.send(cursor_pos_header.encode(FORMAT))
            client.send(cursor_pos.encode(FORMAT))
            client.send(text_to_insert.encode(FORMAT))

            modified_text = client.recv(1024).decode(FORMAT)
            print("Modified Text:")
            print(modified_text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        content_length = int(client.recv(HEADER).decode(FORMAT).strip())
        original_text = client.recv(content_length).decode(FORMAT)
        print("Original Text:")
        print(original_text)

        cursor_pos = input("Enter the cursor position (row,column): ")
        text_to_insert = input("Enter the text to insert: ")

        cursor_pos = f"{cursor_pos:<{HEADER}}"
        client.send(cursor_pos.encode(FORMAT))
        client.send(text_to_insert.encode(FORMAT))

        modified_text_length = int(client.recv(HEADER).decode(FORMAT).strip())
        modified_text = client.recv(modified_text_length).decode(FORMAT)
        print("Modified text:", modified_text)

        send_thread = threading.Thread(target=send_data, args=(client,))
        send_thread.start()
        
        send_thread.join()  
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.send(DISCONNECT_MESSAGE.encode(FORMAT))
        client.close()

if __name__ == "__main__":
    main()
    '''

import socket

HEADER = 10  # Fixed length header for message size
PORT = 8080
FORMAT = "utf-8"
SERVER = "127.0.0.1"  # Assuming the server is running locally
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = f"{msg_length:<{HEADER}}".encode(FORMAT)
    client.send(send_length)
    client.send(message)

try:
    # Receive the original text from the server
    content_length = client.recv(HEADER).decode(FORMAT).strip()
    if content_length:
        content = client.recv(int(content_length)).decode(FORMAT)
        print("Original Content:\n", content)

    # Prompt user to enter cursor position
    cursor_pos = input("Enter cursor position (x,y): ")
    send(cursor_pos)

    # Prompt user to enter text to insert
    text_to_insert = input("Enter text to insert: ")
    send(text_to_insert)

    # Receive the modified text from the server
    modified_content_length = client.recv(HEADER).decode(FORMAT).strip()
    if modified_content_length:
        modified_content = client.recv(int(modified_content_length)).decode(FORMAT)
        print("Modified Content:\n", modified_content)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()





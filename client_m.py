import socket

HEADER = 10
PORT = 7172  # Changed port number
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def main():
    try:
        # Receive the original text from the server
        content_length = int(client.recv(HEADER).decode(FORMAT).strip())
        original_text = client.recv(content_length).decode(FORMAT)
        print("Original Text:")
        print(original_text)

        cursor_pos = input("Enter the cursor position (row,column): ")
        text_to_insert = input("Enter the text to insert: ")

        cursor_pos = f"{cursor_pos:<{HEADER}}"
        client.send(cursor_pos.encode(FORMAT))
        client.send(text_to_insert.encode(FORMAT))

        # Receive the modified text from the server
        modified_text_length = int(client.recv(HEADER).decode(FORMAT).strip())
        modified_text = client.recv(modified_text_length).decode(FORMAT)
        
        print("Modified Text:")
        print(modified_text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.send(DISCONNECT_MESSAGE.encode(FORMAT))
        client.close()

if __name__ == "__main__":
    main()
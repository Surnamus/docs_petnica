import socket

HEADER = 10
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# Create and connect the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def main():
    try:
        # Input the cursor position and text to insert
        cursor_pos = input("Enter the cursor position (row,column): ")
        text_to_insert = input("Enter the text to insert: ")

        # Send the cursor position
        cursor_pos_formatted = f"{cursor_pos:<{HEADER}}"
        client.send(cursor_pos_formatted.encode(FORMAT))

        # Send the text to insert
        client.send(text_to_insert.encode(FORMAT))

        # Receive and print the modified text
        modified_text = client.recv(1024).decode(FORMAT)
        print("Modified Text:")
        result = ''.join(''.join(row) for row in modified_text)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Send the disconnect message and close the connection
        client.send(DISCONNECT_MESSAGE.encode(FORMAT))
        client.close()

if __name__ == "__main__":
    main()

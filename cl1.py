import socket

HEADER = 10
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "127.0.0.1"  # Adjust as needed
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = f"{msg_length:<{HEADER}}".encode(FORMAT)
    client.send(send_length)
    client.send(message)
    response_length = client.recv(HEADER).decode(FORMAT)
    if response_length:
        response_length = int(response_length.strip())
        response = client.recv(response_length).decode(FORMAT)
        return response

def main():
    print("Enter the text matrix (end with an empty line):")
    original_text = []
    while True:
        line = input()
        if line == "":
            break
        original_text.append(line)
    
    insert_text_str = input("Enter the text to insert: ")
    row = int(input("Enter the cursor row position: "))
    column = int(input("Enter the cursor column position: "))
    
    # Prepare the message to send
    message = '|'.join(original_text) + f"|{insert_text_str}|{row}|{column}"
    response = send_message(message)
    print("Modified Text:")
    print(response.replace('|', '\n'))
    
    send_message(DISCONNECT_MESSAGE)

if __name__ == "__main__":
    main()
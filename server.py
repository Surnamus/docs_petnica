import socket

HEADER = 10  # Fixed length header for message size
PORT = 7171
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def findpos(cursor_pos,text,character):
    x=int(int(cursor_pos[0]))
    y=int(cursor_pos[2])
    txtarr=text.split("\n")
    if (x>len(txtarr)-1):
        for i in range(x-len(txtarr)+1):
            txtarr.append("")
               
   # for i in range(0, len(txtarr)):
     # txtarr[i]=list(txtarr[i])
   # for i in range(y,len(character)):
    #    txtarr[x].insert(i,str(character[i]))'''
    txtarr = [list(line) for line in txtarr]

    # Insert the character(s) at the specified position
    for i in range(len(character)):
        txtarr[x].insert(y + i, character[i])    
    result = '\n'.join(''.join(row) for row in txtarr)
    return result
    
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    content = None
    global contentm
    with open("text.txt", 'r+') as f:
        content = f.read()
        cursor_pos = conn.recv(1024).decode()
        print(cursor_pos)
        text=conn.recv(1024).decode()
        contentm=findpos(cursor_pos,content,text)
        f.write(contentm)
    conn.send(contentm.encode())

    
    
    print(f"[DISCONNECTED] {addr} disconnected.")
    conn.close()

def send_message(conn, message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = f"{msg_length:<{HEADER}}".encode(FORMAT)
    conn.send(send_length)
    conn.send(message)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

print("[STARTING] Server is starting...")
start()


import socket
import sys
import os
os.system('cls')
if len(sys.argv) < 3:
    print("Use script as server.py ip port")
    sys.exit(0)
ip = sys.argv[1]
port = int(sys.argv[2])
server = socket.socket()
server.bind((ip, port))
server.listen()
print("Server is listning for clients at {ip}:{port}")
client, caddr = server.accept()
print(f"Connected to a Client at addrs: {caddr}")
while True:
    cmsg = client.recv(1024).decode()
    print(f"client --> {cmsg}".rjust(30))
    if cmsg.lower().strip() == 'endofchat':
        print("Client has disconnected the chat")
        client.close()
        break
    smsg = input('server --> ')
    client.send(smsg.encode())
    if smsg.lower().strip() == 'endofchat':
        print("We have disconnected the chat")
        client.close()
        break
server.close()

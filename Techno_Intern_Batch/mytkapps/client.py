import socket
import os
import sys
os.system('cls')
if len(sys.argv) < 3:
    print('Use Script as client.py server_ip server_port')
    sys.exit(0)
sip = sys.argv[1]
sport = int(sys.argv[2])  
client = socket.socket()
client.connect((sip, sport))
print(f"Got Connected to server {sip}:{sport}")
while True:
    cmsg = input("client --> ")
    client.send(cmsg.encode())
    if cmsg.lower().strip() == 'endofchat': # chat terminatation protocol
        print("We are closing chat application")
        client.close()
        break   
    smsg = client.recv(1024).decode()
    print(f"server --> {smsg}".rjust(30))
    if smsg.lower().strip() == 'endofchat':
        print("Server has closed chat application")
        client.close()
        break

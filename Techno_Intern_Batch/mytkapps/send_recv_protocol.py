"""
    Chat application module for send and recv protocols
    
    send(socket) --> will send message to socket
    recv(socket) --> recv data from socket
"""


def send(socket):
    while True:
        msg = input("You: ")
        socket.send(msg.encode())
        if msg.lower().strip() == 'endofchat':
            return None

def recv(socket):
    while True:
        msg = socket.recv(1024).decode()
        print(f"friend: {msg}".rjust(80))
        if msg.lower().strip() == 'endofchat':
            return None

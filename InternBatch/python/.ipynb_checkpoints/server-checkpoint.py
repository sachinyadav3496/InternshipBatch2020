import socket
server = socket.socket()
# TCP, IPV4
# facebook.com --> DNS --> ip_fb --> (ip_fb, 80)
ip = '192.168.29.232'
port = 1234
server.bind((ip, port))
# it means server will accept all request on port 1234
server.listen(5) # 2nd --> serve , wait 3, 4, 5
print(f"Server is Listining for client at {ip}:{port}")
client, addr = server.accept() # accepting client connection
# addr = (cip, cport)
print(f"\nConnected to a client {addr[0]}:{addr[1]}")
request = client.recv(1024).decode()
# we are recieving client request 
print("Client Request: ", request)
response = "Welcome to the World of Socket Programming".encode()
client.send(response)
client.close()
server.close()
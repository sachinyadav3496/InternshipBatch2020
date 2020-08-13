import socket
client = socket.socket()
server_ip = '192.168.29.232'
server_port = 1234
client.connect((server_ip, server_port))
print("Got Connected to server waiting sending request")
request = "Hello Server, a simple socket request".encode()
client.send(request)
response = client.recv(1024).decode()
print("Sever's Response: ", response)
client.close()
# state less protocol
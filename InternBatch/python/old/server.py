import time
import socket

html = """<!Doctype html>
<html>
    <body>
        <h1 style='color:red'>Hello Welcome My Own Web Server</h1>
        
        <h2 style='color:blue'>This is how Internet Works </h2>
    </body>
</html>
"""

resp = f"""HTTP/1.1 200 OK
Date: {time.ctime()}
Server: Python
ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes
Content-Length: {len(html)}
Content-Type: text/html

{html}
"""
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# family --> ipv4 (socket.AF_INET), ipv6 (socket.AF_INET6)
# type --> tcp (socket.SOCK_STREAM, socket.SOCK_DGRAM)
ip = '192.168.29.232'
port = 80
server.bind((ip, port))
# server is ready
server.listen()

print(f"Server is running at port {port} at ip {ip}")
client, addr = server.accept()

print("Got a connection from client: ", addr)

print(client.recv(1024).decode())
client.send(resp.encode())

client.close()
server.close()

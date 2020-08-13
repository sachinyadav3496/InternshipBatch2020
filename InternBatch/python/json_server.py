import socket
import json
server = socket.socket()
server.bind(('192.168.29.232', 1234))
server.listen()

for var in range(5):
    client, addr = server.accept()
    print(f"client {var+1}: ", addr)
    
    req = json.loads(client.recv(1024))
    
    if req['REQTYPE'] == 'message':
        print(f"User {req['user']} has connected to server")
        resp = { 'msgtype': 'reply', 'info': 'this is called protocall'}
        client.send(json.dumps(resp).encode())
        client.close()
    else:
        resp = json.dumps({ 'msgtype': 'error', 'info': "Invalid Request"}).encode()
        client.send(resp)
        client.close()
        
server.close()
        

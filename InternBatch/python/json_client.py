import socket
import json
import random

client = socket.socket()
client.connect(('192.168.29.232', 1234))

num = random.randint(1, 10)
if num % 2 == 0:
    req = json.dumps({'REQTYPE': 'message', 'user': 'Sachin Yadac'}).encode()
else:
    req = json.dumps({'REQTYPE': 'ha ha ha'}).encode()

client.send(req)

resp = json.loads(client.recv(1024))

if resp['msgtype'] == 'reply':
    print("got inforamtion : ", resp['info'])
else:
    print("Error Response ")
    print(resp['info'])
client.close()

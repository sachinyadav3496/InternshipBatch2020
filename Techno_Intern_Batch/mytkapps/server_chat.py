import socket
from send_recv_protocol import send, recv
import threading
import os
import sys


if __name__ == "__main__":
    os.system('cls')
    print("\n\n\n")
    try:
        if len(sys.argv) < 3 or len(sys.argv) > 3:
            print("Use Script as server_chat.py ip port")
            sys.exit(0)
        else:
            ip   = sys.argv[1]
            port = int(sys.argv[2])
            server = socket.socket()
            server.bind((ip, port))
            server.listen()
            print(f"Server is Waiting for clients at {ip}:{port}")
    except ValueError as e:
        print("port nubmers are integers follow that")
        sys.exit(0)
    except OSError as e:
        print("!!Error in Creating Socket!!", e)
        sys.exit(0)
    
    client, (cip, cport) = server.accept()
    print(f"\nConnected to a client at {cip}:{cport}")
    
    send_th = threading.Thread(target=send, args=(client, ))
    recv_th  = threading.Thread(target=recv, args=(client, ))
    
    send_th.start()
    recv_th.start()
    
    send_th.join()
    recv_th.join()
    
    print("Connection Closed")
    client.close()
    server.close()
    sys.exit(0)

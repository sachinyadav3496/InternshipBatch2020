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
            print("Use Script as client_chat.py ip port")
            sys.exit(0)
        else:
            sip   = sys.argv[1]
            sport = int(sys.argv[2])
            client = socket.socket()
            client.connect((sip, sport))
            
    except ValueError as e:
        print("port nubmers are integers follow that")
        sys.exit(0)
    except OSError as e:
        print("!!Error in Creating Socket!!", e)
        sys.exit(0)
    
    print(f"\nConnected to a server at {sip}:{sport}")
    
    send_th = threading.Thread(target=send, args=(client, ))
    recv_th  = threading.Thread(target=recv, args=(client, ))
    
    send_th.start()
    recv_th.start()
    
    send_th.join()
    recv_th.join()
    
    print("Connection Closed")
    client.close()
    
    sys.exit(0)

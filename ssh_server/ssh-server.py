import sys
import threading
import paramiko
import socket
import traceback
from request_handler import request_handler
host_key = paramiko.RSAKey(filename='../keys/sluicekey.pem')
#print(host_key)

class ssh_server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()

    def check_auth_publickey(self, username, key):
        publicKey = request_handler.get_publicKey(username)
        if (key == publicKey):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.OPEN_FAILED_ADMINISTRATIVERY_PROHIBITED

    
# now connect
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 2200))
except Exception as e:
    print('*** Bind failed: ' + str(e))
    traceback.print_exc()
    sys.exit(1)

try:
    sock.listen(100)
    print('Listening for connection ...')
    client, addr = sock.accept()
except Exception as e:
    print('*** Listen/accept failed: ' + str(e))
    traceback.print_exc()
    sys.exit(1)

print('Got a connection!')



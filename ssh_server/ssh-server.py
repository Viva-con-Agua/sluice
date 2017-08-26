import sys

from binascii import hexlify
import threading
import paramiko
import socket
import traceback
import gssapi
from request_handler import request_handler
from paramiko.py3compat import b, u, decodebytes


host_key = paramiko.RSAKey(filename='../keys/sluice_rsa')
#print(host_key)
print('Read key: ' + u(hexlify(host_key.get_fingerprint())))
class ssh_server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()
    
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_publickey(self, username, key):
        print('Auth attempt with key: ' + u(hexlify(key.get_fingerprint())))
        if username == 'test':
            publicKey = request_handler.get_publicKey(username)
            print(publicKey)
            if (key == publicKey):
                return paramiko.AUTH_SUCCESSFUL
        return paramiko.OPEN_FAILED_ADMINISTRATIVERY_PROHIBITED

    def check_channel_env_request(self, channel, name, value):
        #if name == 'INVALID_ENV':
        #    return False
        if name != 'DROPS':
            return False
        else:
            response = request_handler.handle_ssh_request(value)
            chan.send(response)
            return True
        
        #if not hasattr(channel, 'env'):
        #    setattr(channel, 'env', {})

        #channel.env[name] = value
        #return True
#UseGSSAPI = True 
DoGSSAPIKeyExchange = True    
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

try:
    t = paramiko.Transport(client)
    try:
        t.load_server_moduli()
    except:
        print('Failed to load moduli')
        raise
    t.add_server_key(host_key)
    server = ssh_server()
    try:
        t.start_server(server=server)
    except paramiko.SSHException:
        print('*** SSH negotiation failed.')
        sys.exit(1)
    chan = t.accept(None)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)
    print('Authenticated!')
except Exception as e:
    print('*** Caught exception: ' + str(e.__class__) + ': ' + str(e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)

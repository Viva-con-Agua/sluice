import sys

from binascii import hexlify
import threading
import paramiko
import socket
import traceback
from ssh_server.request_handler import request_handler
from paramiko.py3compat import b, u, decodebytes
import base64
from sshpubkeys import SSHKey

host_key = paramiko.RSAKey.from_private_key_file('keys/sluice_key')
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
        try:
            KEY = paramiko.pkey.PKey.get_base64(key)
            
            publicKey = request_handler.get_publicKey(username)
            if(isinstance( publicKey, int ) != True):
                pub = publicKey.split(' ')
                if (KEY == pub[1]):
                    return paramiko.AUTH_SUCCESSFUL
                else:
                    return paramiko.Auth_FAILED
            else:
                return paramiko.AUTH_FAILED
        except Exception as e:
            print(e)
            return paramiko.AUTH_FAILED

    def check_channel_env_request(self, channel, name, value):
        if name != 'DROPS':
            return False
        else:
            response = request_handler.handle_ssh_request(value)
            chan.send(response)
            return True

    def enable_auth_gssapi(self):
        return True
 
    def get_allowed_auths(self, username):
        return 'publickey'

    # now connect
    def start_socket(self):
        DoGSSAPIKeyExchange = True    
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
               #sys.exit(1)
           print('Authenticated!')
        except Exception as e:
           print('*** Caught exception: ' + str(e.__class__) + ': ' + str(e))
           traceback.print_exc()
           try:
               t.close()
           except:
               pass
           sys.exit(1)

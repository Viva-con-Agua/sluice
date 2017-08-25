import sys

import threading
import paramiko
import socket
import traceback
import gssapi
from request_handler import request_handler
host_key = paramiko.RSAKey(filename='../keys/sluice_rsa')
#print(host_key)

class ssh_server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()

    def check_auth_publickey(self, username, key):
        publicKey = request_handler.get_publicKey(username)
        print(publicKey)
        if (key == publicKey):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_SUCCESSFUL
    def check_auth_gssapi_with_mic(self, username,
                                   gss_authenticated=paramiko.AUTH_FAILED,
                                   cc_file=None):
        """
        .. note::
            We are just checking in `AuthHandler` that the given user is a
            valid krb5 principal! We don't check if the krb5 principal is
            allowed to log in on the server, because there is no way to do that
            in python. So if you develop your own SSH server with paramiko for
            a certain platform like Linux, you should call ``krb5_kuserok()`` in
            your local kerberos library to make sure that the krb5_principal
            has an account on the server and is allowed to log in as a user.
        .. seealso::
            `krb5_kuserok() man page
            <http://www.unix.com/man-page/all/3/krb5_kuserok/>`_
        """
        if gss_authenticated == paramiko.AUTH_SUCCESSFUL:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_auth_gssapi_keyex(self, username,
                                gss_authenticated=paramiko.AUTH_FAILED,
                                cc_file=None):
        if gss_authenticated == paramiko.AUTH_SUCCESSFUL:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED 


    def enable_auth_gssapi(self):
        return True


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
    t = paramiko.Transport(client, gss_kex=DoGSSAPIKeyExchange)
    t.set_gss_host(socket.getfqdn(""))
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
    chan = t.accept(20)
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

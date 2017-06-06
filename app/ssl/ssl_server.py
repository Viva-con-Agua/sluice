from bottle import Bottle, run, request, server_names, ServerAdapter

class ssl_server(ServerAdapter):
    def run(self, handler):
        from cherrypy import _cpwsgiserver3
        server = _cpwsgiserver3.CherryPyWSGIServer((self.host, self.port), handler)
    
        # If cert variable is has a valid path, SSL will be used
        # You can set it to None to disable SSL
        cert = '/var/tmp/server.pem' # certificate path 
        server.ssl_certificate = cert
        server.ssl_private_key = cert
        try:
            server.start()
        finally:
            server.stop()

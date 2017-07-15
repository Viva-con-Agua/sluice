import sys, getopt
from app.webserver import webserver
from app.authservice import authservice
from cherrypy._cpserver import Server
import cherrypy
if __name__ == '__main__':
    server_config={
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080
            }
    cherrypy.config.update(server_config)
    cherrypy.tree.mount(webserver(),'/')
    cherrypy.tree.mount(authservice(), '/auth')
    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.stop()



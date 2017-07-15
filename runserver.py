import sys, getopt
from app.webserver import webserver
from app.authservice import authservice
from cherrypy._cpserver import Server
import cherrypy
def main(argv):
    privatekey = ''
    
    try:
        opts, args = getopt.getopt(argv, "hp:", ["privateKey="])
    except getopt.GetoptError:
        print('runserver.py -p <privateKey>')
        sys.exit(2)  
    for opt, arg in opts:
        if opt == '-h':
            print('runserver.py -p <privateKey>')
            sys.exit()
        elif opt in ("-p", '--privateKey'):
            privatekey = arg
if __name__ == '__main__':
   # main(sys.argv[1:])
    
    server_config={#'/':
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080
        }
    auth_config={'/auth':
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8000
        }


#    authserver = Server()
#    authserver.socket_host = '0.0.0.0'
#    authserver.socket_port = 8000
#    authserver.instance = authservice()
#    authserver.subscribe()

    cherrypy.config.update(server_config)
    cherrypy.tree.mount(webserver(), '/')
    #auth = authservice()
    #auth.socket_port = 8000
    #auth.subscribe()
    cherrypy.tree.mount(authserver() '/auth')

    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.stop()
#cherrypy.config.update({'engine.autoreload.on': False})
#cherrypy.server.unsubscribe()
#cherrypy.engine.start()
#wsgiapp = cherrypy.tree.mount(webserver())



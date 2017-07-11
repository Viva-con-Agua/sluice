import sys, getopt
from app.webserver import webserver
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
#if __name__ == '__main__':
   # main(sys.argv[1:])
cherrypy.config.update({'engine.autoreload.on': False})
cherrypy.server.unsubscribe()
cherrypy.engine.start()
wsgiapp = cherrypy.tree.mount(webserver())

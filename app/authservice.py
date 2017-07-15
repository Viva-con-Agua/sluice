import cherrypy

class authservice(object):

    @cherrypy.expose
    def index(self):
        return "authservice"



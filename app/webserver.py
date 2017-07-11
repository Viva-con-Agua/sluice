from app.auth import *
from app.daos import *
from app.models.microservice import microservice
from bottle import Bottle, route, run, request, static_file, template
import copy
import cherrypy
key = ''

class webserver(object):

   # sluice = Bottle()
   # login = login()
   # shared_session = shared_session()
   # db = microserviceDAO()


    #def __init__(self, key):
    #    self.key = key

    #@sluice.route('/')
    @cherrypy.expose
    def index(self):
        return "sluice manual: coming soon"
   
    
    #@sluice.route('/api/addMicro', method='POST')
    @cherrypy.expose
    def addMicro(self, name, url, version):
        microS = microservice()
        micro = copy.deepcopy(microS.Microservice)
        micro['name'] = name
        micro['url'] = url
        micro['version'] = version
        db = microserviceDAO()
        db.add(micro)


    

    #@sluice.route('/signupMicro')
    @cherrypy.expose
    def signupMicro(self):
        return """<html>
          <head></head>
          <body>
            <form method="post" action="addMicro">
              <input type="text" value="" name="name" />
              <input type="text" value="" name="url" />
              <input type="text" value="" name="version" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    
    #@sluice.route('/javascripts/<filename>')
    @cherrypy.expose
    def server_static(self, filename):
        return static_file(filename, root='public/javascripts')

    #@sluice.route('/authRSA')
    @cherrypy.expose
    def authRSA(self):
        microName = request.query.microName
        token = request.query.token
        if token == '' or microName == '':
            return('login fail')
        else:
            print('DEBUG: ' + token + ' ' + microName + '\n')
            payload = login.vertifyToken_RS512(name, token)
            sharedSession = shared_session.create_token(payload, self.key)
            return sharedSession
    
    #def runserver(self): 
    #   run(webserver.sluice, host='localhost', port=8080)



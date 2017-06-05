from app.auth import *

from bottle import Bottle, route, run, request, static_file, template

key = ''

class webserver:

    sluice = Bottle()
    login = login()
    shared_session = shared_session()


    def __init__(self, key):
        self.key = key

    @sluice.route('/')
    def index():
        return "sluice manual: coming soon"
    

    @sluice.route('/signupMicro')
    def signupMicro():
        return template('./app/views/index.html')

    @sluice.route('/javascripts/<filename>')
    def server_static(filename):
        return static_file(filename, root='public/javascripts')

    @sluice.route('/authRSA')
    def authRSA():
        microName = request.query.microName
        token = request.query.token
        if token == '' or microName == '':
            return('login fail')
        else:
            print('DEBUG: ' + token + ' ' + microName + '\n')
            payload = login.vertifyToken_RS512(name, token)
            sharedSession = shared_session.create_token(payload, self.key)
            return sharedSession
    
    def runserver(self): 
        run(webserver.sluice, host='localhost', port=8080)



from auth import *

from bottle import Bottle, route, run


sluice = Bottle()
login = login()
shared_session = shared_session()



@sluice.route('/')
def index():
    return "sluice manual: coming soon"

@sluice.route('/authRSA')
def authRSA():
    microName = request.query.microName
    token = request.query.token
    payload = login.vertifyToken_RS512(name, token)
    sharedSession = shared_session.create_token(payload)
    return sharedSession

run(sluice, host='localhost', port=8080)


from jose import jws
from jose.exceptions import JWSError


class login(object)

    def __init__(self):
        self.microDB = microserviceDAO
    
   

    # check if token verify and return payload
    # will use RSA and SHA512 for sign check
    def verifyToken_RS512(self, token, name):

        # key == publicKey of the microservice
        key = self.microDB.get_Key(name)
        if key == False:
            
            # if there is no MS named "name", return JWSError
            return JWSError('Microservice is not registrate')
        else:

            # verify token return payload
            payload = jws.verify(token, key, algorithms='RS512')
        return payload
        

        

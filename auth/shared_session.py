from jose import jwt
from models import payload
import copy


class shared_session(object):
    
    def __init__(object):
        self.payload = payload()

    def create_payload(login_payload):
        payload = copy.deepcopy(self.payload.Payload)
        payload.micro = login_payload.micro

        # permission handling not ready
        payload.access_to = login_payload.access_to
        return payload

    def create_token(payload, key):
        token = jwt.encode(payload, key, algorithm='RS512')
        return token



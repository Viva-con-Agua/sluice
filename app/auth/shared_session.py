from jose import jwt
from app.models import payload
import copy


class shared_session(object):

    def create_token(login_payload, key):
        payload = copy.deepcopy(payload.Payload)
        payload.micro = login_payload.micro

        # permission handling not ready
        payload.access_to = login_payload.access_to
        token = jwt.encode(payload, key, algorithm='RS512')
        return token



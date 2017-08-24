import requests
import jwt
import json
import pem
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
#jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

class request_handler(object):
    KEY = pem.parse_file('../keys/sluicekey.pem')
    print(str(KEY[0]))
    def get_payload(name):
        payload = requests.get('http://localhost:8000/api/payload/' + name)
        payload_json = json.dumps(payload.text)
        print(payload.text)
        token = jwt.encode({'hallo': 'hallo'}, str(request_handler.KEY[0]), algorithm='RS512')
        return token


print(request_handler.get_payload('blub'))

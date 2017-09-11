import requests
import jwt
import json
import pem
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
#jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

class request_handler(object):
    #KEY = pem.parse_file('../keys/sluicekey.pem')

    def get_token(name):
        payload = requests.get('http://localhost:8000/api/payload/' + name)
        KEY = pem.parse_file('../keys/sluicekey.pem')
        print(payload.status_code)
        payload_json = json.loads(payload.text)
        print(payload.text)
        token = jwt.encode(payload_json, str(KEY[0]), algorithm='RS512')
        return token

    def get_publicKey(name):
        payload = requests.get('http://localhost:8000/api/payload/' + name)
        if payload.status_code != 200:
            return payload.status_code
        else:
            payload_json = json.loads(payload.text)
            publicKey = payload_json['publicKey']
            print(publicKey)
            return publicKey

    def handle_ssh_request(request):
        return requests(request)

#print(request_handler.get_token('blub'))
#print(request_handler.get_publicKey('blb'))

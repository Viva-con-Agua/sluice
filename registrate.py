import sys, getopt
from app.models import microservice
import rsa

def main(argv):
    privatekey = ''
    name = ''
    try:
        opts, args = getopt.getopt(argv, "n:k:", ["privateKey="])
    except getopt.GetoptError:
        print('runserver.py -p <privateKey>')
        sys.exit(2)  
    for opt, arg in opts:
        if opt == '-h':
            print('runserver.py -p <privateKey>')
            sys.exit()
        elif opt in ("-n", '--name'):
            name = arg
        elif opt in ("-k", '--publicKey'):
            publickey = arg
    if publickey == '' or name == '':
        print('registrate.py -n <name> -k <publicKey>')
        sys.exit()
    else:
        with open(publickey, 'r') as keyfile:
            keydata = keyfile.read()
            print(keydata)
        
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(keydata)
        print(pubkey)

if __name__ == '__main__':
    main(sys.argv[1:])

import sys, getopt
from daos import *
from models import microservice


def main(argv):
    privatekey = ''
    
    try:
        opts, args = getopt.getopt(argv, "hp:", ["privateKey="])
    except getopt.GetoptError:
        print('runserver.py -p <privateKey>')
        sys.exit(2)  
    for opt, arg in opts:
        if opt == '-h':
            print('runserver.py -p <privateKey>')
            sys.exit()
        elif opt in ("-p", '--privateKey'):
            privatekey = arg

if __name__ == '__main__':
    main(sys.argv[1:])
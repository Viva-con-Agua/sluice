#!/bin/bash

openssl genrsa -out $1.pem 4096
openssl rsa -in $1.pem -pubout > $1.pub

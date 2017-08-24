#!/bin/bash

openssl genrsa -out sluicekey.pem 4096
openssl rsa -in sluicekey.pem -pubout > sluicekey.pub

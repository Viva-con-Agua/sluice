openssl x509 -req -days 365 -in sluice.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out sluice.crt

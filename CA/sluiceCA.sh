openssl genrsa -out sluice.key 4096
openssl req -new -key sluice.key -out sluice.csr

#FROM tiangolo/uwsgi-nginx-flask:flask
#FROM haproxy:1.7
#COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

# copy over our requirements.txt file
#COPY requirements.txt /tmp/

# upgrade pip and install required python packages
#RUN pip install -U pip
#RUN pip install -r /tmp/requirements.txt

# copy over our app code
#COPY ./app /app

# set an environmental variable, MESSAGE,
# which the app will use and display
#ENV MESSAGE "hello from Docker"

FROM python:3-onbuild
#CMD [ "python", "./runserver.py" ]
CMD [ "python", "./run-auth-server.py" ]

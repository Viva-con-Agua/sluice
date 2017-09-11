FROM python:3.4-alpine

ADD VERSION .
#Requirements for Docker OS
ADD requirements.txt /requirements.txt

RUN set -ex \
	&& apk add --no-cache --virtual .build-deps \
		gcc \
		make \
		libc-dev \
		musl-dev \
		linux-headers \
		pcre-dev \
		libffi-dev \
		libgss-dev \
		postgresql-dev\
		dovecot-gssapi \
	&& apk add tmux --no-cache \
	&& pyvenv /venv \
  && /venv/bin/pip install -U pip \
  && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
 	&& runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
  )" \
  && apk add --virtual .python-rundeps $runDeps \
  && apk del .build-deps

RUN mkdir /sluice/
WORKDIR /sluice/
ADD . /sluice/

EXPOSE 8000

CMD ["/bin/sh", "-c", "tmux new -AdDEP /venv/bin/python manage.py runserver 0.0.0.0:8000 && tmux new -AdDEP /venv/bin/python ssh_server/ssh-server.py"]
#CMD ["/bin/sh", "-c", "tmux new -AdDEP /venv/bin/python ssh_server/ssh-server.py"]


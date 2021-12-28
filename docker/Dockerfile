FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app/ProtoAF
WORKDIR /usr/src/app/ProtoAF

ADD shell.sh /usr/local/bin/shell.sh
RUN chmod 777 /usr/local/bin/shell.sh

EXPOSE 8000

CMD /usr/local/bin/shell.sh ; sleep infinity
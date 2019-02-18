FROM python:3.7.2-slim-stretch

ADD src /app/src
ADD setup.py /app

WORKDIR /app

RUN python setup.py develop

CMD ["bin", "start", "--port=8080"]

EXPOSE 8080

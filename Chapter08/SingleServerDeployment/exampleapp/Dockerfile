FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y nodejs npm

ADD app.js /var/www/app.js
ADD package.json /var/www/package.json

WORKDIR /var/www
RUN npm install

CMD nodejs app.js

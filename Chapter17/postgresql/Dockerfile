FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y postgresql-9.3

WORKDIR /etc/postgresql/9.3/main
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" postgresql.conf
RUN echo "host all all 0.0.0.0/0 password" >> pg_hba.conf

EXPOSE 5432

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT /entrypoint.sh

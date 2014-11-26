FROM centos:centos7

RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
RUN yum install -y python-pip python-devel nginx gcc

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD exampleapp.conf /etc/nginx/conf.d/exampleapp.conf

WORKDIR /tmp
ADD oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm /tmp/
ADD oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm /tmp/
RUN yum install -y oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
RUN yum install -y oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm
RUN rm -rf *.rpm

ENV ORACLE_HOME /usr/lib/oracle/12.1/client64
RUN echo "/usr/lib/oracle/12.1/client64/lib" > /etc/ld.so.conf.d/oracle.conf && ldconfig
RUN pip install django gunicorn cx_Oracle

ADD ./ /var/www/exampleapp
WORKDIR /var/www/exampleapp
RUN chmod +x entrypoint.sh
RUN rm -rf *.rpm

EXPOSE 80

ENTRYPOINT ./entrypoint.sh

FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y nginx \
    git make pbuilder python-mock python-configobj \
    python-support cdbs

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

WORKDIR /tmp
RUN git clone https://github.com/BrightcoveOS/Diamond.git
RUN cd Diamond && git checkout v3.4 && make deb
RUN dpkg -i Diamond/build/diamond_3.4.0_all.deb
RUN cp /etc/diamond/diamond.conf.example /etc/diamond/diamond.conf

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80
EXPOSE 443

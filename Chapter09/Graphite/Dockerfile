FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install curl

RUN curl -s http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb http://packages.elasticsearch.org/elasticsearch/1.0/debian stable main" > /etc/apt/sources.list.d/elasticsearch.list
RUN apt-get update

RUN apt-get install -y graphite-carbon
RUN echo "CARBON_CACHE_ENABLED=true" > /etc/default/graphite-carbon

RUN apt-get install -y graphite-web apache2 apache2-mpm-worker libapache2-mod-wsgi
RUN sudo -u _graphite graphite-manage syncdb --noinput
RUN rm -f /etc/apache2/sites-enabled/000-default.conf
RUN cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-enabled/graphite.conf

RUN apt-get install -y elasticsearch openjdk-7-jre-headless
RUN update-rc.d elasticsearch defaults

RUN apt-get install -y nodejs npm
RUN ln -s /usr/bin/nodejs /usr/local/bin/node
RUN curl https://codeload.github.com/grafana/grafana/tar.gz/v1.7.0 | tar -xz
RUN mv grafana-1.7.0 /usr/share/grafana
WORKDIR /usr/share/grafana
RUN npm install
RUN node_modules/grunt-cli/bin/grunt
RUN echo "alias /grafana /usr/share/grafana/src" > /etc/apache2/sites-enabled/grafana.conf
ADD config.js /usr/share/grafana/src/config.js

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

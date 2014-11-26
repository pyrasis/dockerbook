FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev git
RUN apt-get install -y nginx nodejs curl libmysqlclient-dev

RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build
ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH

ENV CONFIGURE_OPTS --disable-install-doc
RUN rbenv init -
RUN rbenv install 2.1.3
RUN rbenv global 2.1.3

RUN echo 'gem: --no-rdoc --no-ri' >> /root/.gemrc
RUN gem install bundler
RUN rbenv rehash

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/sites-enabled/default
ADD exampleapp.conf /etc/nginx/sites-enabled/exampleapp.conf

WORKDIR /tmp
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN bundle install

ADD ./ /var/www/exampleapp
WORKDIR /var/www/exampleapp
RUN chmod +x entrypoint.sh

EXPOSE 80

ENTRYPOINT ./entrypoint.sh

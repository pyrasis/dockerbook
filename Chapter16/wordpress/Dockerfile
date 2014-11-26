FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y apache2 php5 php5-mysql mysql-client wget

WORKDIR /var/www
RUN wget http://ko.wordpress.org/wordpress-4.0-ko_KR.tar.gz -O - | tar -xz

WORKDIR /etc/apache2/sites-enabled
RUN sed -i "s/\/var\/www\/html/\/var\/www\/wordpress/g" 000-default.conf

WORKDIR /var/www/wordpress
RUN mv wp-config-sample.php wp-config.php
RUN sed -i "s/'database_name_here'/'wp'/g" wp-config.php && \
    sed -i "s/'username_here'/'root'/g" wp-config.php && \
    sed -i "s/'password_here'/getenv('DB_ENV_MYSQL_ROOT_PASSWORD')/g" wp-config.php && \
    sed -i "s/'localhost'/'db'/g" wp-config.php

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT /entrypoint.sh

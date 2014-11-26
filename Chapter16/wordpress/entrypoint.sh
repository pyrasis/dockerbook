#!/bin/sh

mysql -h db -uroot -p$DB_ENV_MYSQL_ROOT_PASSWORD -e "create database wp"
apachectl -DFOREGROUND

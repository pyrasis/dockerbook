#!/bin/bash

sed -i "s/host = graphite/host = $GRAPHITE_HOST/g" /etc/diamond/diamond.conf
diamond

cd /etc/nginx
nginx

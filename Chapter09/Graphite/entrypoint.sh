#!/bin/bash

service carbon-cache start
service elasticsearch start

apachectl -DFOREGROUND

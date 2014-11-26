#!/bin/bash

if [ -z $POSTGRESQL_PASSWORD ]; then
  exit 1
fi

POSTGRESQL_BIN=/usr/lib/postgresql/9.3/bin/postgres
POSTGRESQL_CONFIG_FILE=/etc/postgresql/9.3/main/postgresql.conf

POSTGRESQL_SINGLE="sudo -u postgres $POSTGRESQL_BIN --single --config-file=$POSTGRESQL_CONFIG_FILE"
$POSTGRESQL_SINGLE <<< "ALTER USER postgres PASSWORD '$POSTGRESQL_PASSWORD';" > /dev/null

exec sudo -u postgres $POSTGRESQL_BIN --config-file=$POSTGRESQL_CONFIG_FILE

#!/bin/bash

if [ -z $MYSQL_ROOT_PASSWORD ]; then
  exit 1
fi

mysql_install_db --user mysql > /dev/null

cat > /tmp/sql <<EOF
USE mysql;
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
UPDATE user SET password=PASSWORD("$MYSQL_ROOT_PASSWORD") WHERE user='root';
EOF

mysqld --bootstrap --verbose=0 < /tmp/sql
rm -rf /tmp/sql

mysqld

#!/bin/bash

if [ -z $ORACLE_PASSWORD ]; then
  exit 1
fi

echo "export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe" > /etc/profile.d/oracle.sh
echo "export ORACLE_SID=XE" >> /etc/profile.d/oracle.sh
echo "export PATH=$PATH:/u01/app/oracle/product/11.2.0/xe/bin" >> /etc/profile.d/oracle.sh
source /etc/profile.d/oracle.sh

printf 8080\\n1521\\n$ORACLE_PASSWORD\\n$ORACLE_PASSWORD\\nn | /etc/init.d/oracle-xe configure
echo "root:$ORACLE_PASSWORD" | chpasswd

/usr/sbin/sshd -D

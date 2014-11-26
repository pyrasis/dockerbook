FROM centos:centos7

RUN yum install -y net-tools bc openssh-server
RUN rm -rf /var/lock
RUN mkdir -p /var/lock/subsys

WORKDIR /tmp
ADD oracle-xe-11.2.0-1.0.x86_64.rpm /tmp/
RUN yum install -y oracle-xe-11.2.0-1.0.x86_64.rpm
RUN rm -rf oracle-xe-11.2.0-1.0.x86_64.rpm

WORKDIR /u01/app/oracle/product/11.2.0/xe/config/scripts
RUN sed -i "s/memory_target/#memory_target/g" init.ora
RUN sed -i "s/memory_target/#memory_target/g" initXETemp.ora
RUN echo -e "pga_aggregate_target=200540160\nsga_target=601620480" >> init.ora
RUN echo -e "pga_aggregate_target=200540160\nsga_target=601620480" >> initXETemp.ora

RUN sed -i "s/#PermitRootLogin/PermitRootLogin/g" /etc/ssh/sshd_config
RUN sshd-keygen

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22
EXPOSE 1521
EXPOSE 8080

ENTRYPOINT /entrypoint.sh

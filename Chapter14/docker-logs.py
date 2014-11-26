import docker
import time

c = docker.Client(base_url='unix://var/run/docker.sock')
c.pull('ubuntu', tag='14.04')
container_id = c.create_container(
  image='ubuntu:14.04',
  command='/bin/bash -c "while sleep 1; do echo 1; done"',
)
c.start(container_id)
time.sleep(5)
print c.logs(container_id)

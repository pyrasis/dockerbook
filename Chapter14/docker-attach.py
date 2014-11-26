import docker
import dockerpty

c = docker.Client(base_url='unix://var/run/docker.sock')
container_id = c.create_container(
  image='ubuntu:14.04',
  stdin_open=True,
  tty=True,
  command='/bin/bash'
)

dockerpty.start(c, container_id)

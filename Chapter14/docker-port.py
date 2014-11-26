import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
container_id = c.create_container(
  image='nginx:latest',
  ports=[80],
  volumes=['/data']
)
c.start(
  container_id,
  port_bindings={80: ('0.0.0.0', 80)}
)
print c.port(container_id, 80)

import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.pull(repository='nginx', tag='latest')
container_id = c.create_container(
  image='nginx:latest',
  ports=[80],
  volumes=['/data'],
  name='hello'
)
c.start(
  container_id,
  port_bindings={80: ('0.0.0.0', 80)},
  binds={'/data': {'bind': '/data', 'ro': False}}
)

import docker
from os.path import expanduser
home = expanduser('~')

tls_config = docker.tls.TLSConfig(
  client_cert=(home + '/.docker/cert.pem', home + '/.docker/key.pem'),
  ca_cert=home + '/.docker/ca.pem',
  verify=True
)
c = docker.Client(base_url='https://docker.example.com:2376', tls=tls_config)
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

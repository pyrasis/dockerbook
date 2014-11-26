import docker
import tarfile
import io

c = docker.Client(base_url='unix://var/run/docker.sock')
container_id = c.create_container(
  image='nginx:latest',
  ports=[80],
  volumes=['/data']
)
c.start(container_id)
response = c.copy(container_id, '/etc/nginx.conf')
t = tarfile.open(fileobj=io.BytesIO(response.data))
t.extractall();

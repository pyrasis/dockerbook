import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.build(
  path='github.com/pyrasis/dind.git',     # GitHub
  #path='http://example.com/Dockerfile',  # http
  tag='hello:0.1', quiet=True, rm=True
)

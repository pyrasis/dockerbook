import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.build(path='.', tag='hello:0.1', quiet=True, rm=True)

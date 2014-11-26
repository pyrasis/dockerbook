import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.import_image(src='./nginx.tar', repository='hello', tag='0.1')

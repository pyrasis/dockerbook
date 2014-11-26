import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
print c.inspect_image('nginx:latest')

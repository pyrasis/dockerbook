import docker

script = open('./hello.tar.gz', 'r')

c = docker.Client(base_url='unix://var/run/docker.sock')
c.build(tag='hello:0.1', quiet=True, fileobj=script, 
        rm=True, custom_context=True, encoding='gzip')

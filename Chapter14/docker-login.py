import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.login(username='exampleuser',
        password='examplepassword',
        email='exampleuser@example.com')

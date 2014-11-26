import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
#c.push(repository='localhost:5000/hello', tag='0.1') # 개인 저장소

c.login(username='exampleuser',
        password='examplepassword',
        email='exampleuser@example.com')
c.push(repository='exampleuser/hello', tag='0.1')     # Docker Hub

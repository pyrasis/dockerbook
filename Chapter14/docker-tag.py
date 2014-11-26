import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
#c.tag('hello:0.1', 'localhost:5000/hello', '0.1')  # 개인 저장소
c.tag('hello:0.1', 'exampleuser/hello', '0.1')      # Docker Hub
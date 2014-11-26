import docker

c = docker.Client(base_url='unix://var/run/docker.sock')
c.pull(repository='nginx', tag='latest')
container_id = c.create_container(
  image='nginx:latest',
  ports=[80],
  volumes=['/data']
)
c.commit(
  container_id,
  repository='hello',
  tag='0.1',
  message='example message',
  author='Hong, Gildong <gd@yuldo.com>',
  conf={
    'Hostname':'',
    'User':'',
    'Memory':0,
    'MemorySwap':0,
    'AttachStdin':False,
    'AttachStdout':False,
    'AttachStderr':True,
    'PortSpecs':None,
    'Tty':False,
    'OpenStdin':False,
    'StdinOnce':False,
    'Env':None,
    'Cmd':[
      '/bin/bash'
    ],
    'Volumes':{
      '/data':{}
    },
    'WorkingDir':'',
    'DisableNetwork':False,
    'ExposedPorts':{
      '80/tcp':{}
    }
  }
)

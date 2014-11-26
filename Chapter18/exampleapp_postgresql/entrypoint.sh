#!/bin/bash

gunicorn exampleapp.wsgi -b unix:/tmp/gunicorn.sock -D
nginx

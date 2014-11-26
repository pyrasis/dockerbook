#!/bin/bash

RAILS_ENV=${RAILS_ENV:-"development"}

bundle exec unicorn -D -c unicorn.rb
nginx

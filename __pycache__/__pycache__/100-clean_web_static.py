#!/usr/bin/python3
""" Web Server """
from fabric.api import env, local, run


env.hosts = ['54.157.184.108', '52.3.248.81']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes out-of-date archives """

    number = int(number)

    number = 2 if number == 0 else number + 1

    directory = '/data/web_static/releases'
    with cd('/versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))

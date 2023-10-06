#!/usr/bin/python3
""" Web Server """
from fabric.api import env, local, run


env.hosts = ['54.157.184.108', '52.3.248.81']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes out-of-date archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    directory = '/data/web_static/releases'
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(directory, number))

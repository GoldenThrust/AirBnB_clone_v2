#!/usr/bin/python3
""" Web Server """
import os
from fabric.api import run, put, env

env.hosts = ['54.157.184.108', '52.3.248.81']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    if not os.path.exists(archive_path):
        return False

    try:
        arch_filename = os.path.basename(archive_path)
        new_path = '/data/web_static/releases/{}'.format(
                    arch_filename[:-4])
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(new_path))
        run("tar -xzf {} -C {}".format(arch_filename,
                                            new_path))

        run("rm /tmp/{}".format(arch_filename))

        run("mv {}/web_static/* {}/".format(new_path, new_path))
        run("rm -rf {}/web_static".format(new_path))

        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_path))
        return True
    except Exception:
        return  False

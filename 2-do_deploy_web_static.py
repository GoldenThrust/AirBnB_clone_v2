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
    
    arch_file = archive_path[9:]
    new_path = arch_file[:-4]
    put(archive_path, "/tmp/" )

    run("sudo mkdir -p {}".format(new_path))
    run("sudo tar -xzf {} -C {}/".format(arch_file,
                                            new_path))
    run("sudo rm {}".format(arch_file))
    run("sudo mv {}/web_static/* {}".format(new_path,
                                            new_path))
    run("sudo rm -rf {}/web_static".format(new_path))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(new_path))
    return True
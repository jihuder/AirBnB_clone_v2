#!/usr/bin/python3
# Factory creates File for do_deploy.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.user = 'ubuntu'
env.hosts = ["34.74.85.117", "52.90.223.70"]


def do_pack():

    """tgz format"""
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        name = "web_static_" + date + ".tgz"
        path = "versions/" + name
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """ creates and distributes an archive to your web servers """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

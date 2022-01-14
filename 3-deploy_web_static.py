#!/usr/bin/python3
""" Genaera tgz files in the server """
from fabric.api import *
import datetime
import os.path
env.hosts = ['34.74.85.117', '52.90.223.70']


def do_pack():
    """ Create file .tgz """
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static_" + date_time + ".tgz"
    localpth = "web_static/"
    local("mkdir -p versions")
    result = local("tar -zcvf {} {}".format(name_file, localpth))
    if result is None:
        return None
    else:
        return name_file


def do_deploy(archive_path):
    """ Create file to server """
    file_name = archive_path.split("/")[-1]
    file_wext = file_name.split(".")[0]
    path = "/data/web_static/releases/"
    if os.path.exists(archive_path) is False:
        return False

    put(archive_path, "/tmp/")
    run("mkdir -p {}{}".format(path, file_wext))
    run("tar -xzf /tmp/{} -C {}{}".format(file_name, path, file_wext))
    run("rm /tmp/{}".format(file_name))
    run("mv {}{}/web_static/* {}{}/".format(path, file_wext, path, file_wext))
    cmd = "rm -rf /data/web_static/releases/"
    run("{}{}/web_static".format(cmd, file_wext))
    run("rm -rf /data/web_static/current")
    command = "ln -s /data/web_static/releases/{}".format(file_wext)
    command += " /data/web_static/current"
    run(command)
    return True


def deploy():
    """ Deploy content """
    file = do_pack()
    if file is None:
        return False
    else:
        print(file)
        do_deploy(file)
    return True

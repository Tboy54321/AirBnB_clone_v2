#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ["18.233.64.67", "52.4.93.199"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """Archiving all web static files file"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    now = datetime.now()
    formatted_time = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(formatted_time)
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, size))
    except Exception:
        archive_name = None
    return archive_name


def do_deploy(archive_path):
    """Deployment"""
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
            newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
            newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False


def deploy():
    """Distributing archive to web servers"""
    archived_path = do_pack()
    if archived_path is None:
        return False
    return do_deploy(archived_path)

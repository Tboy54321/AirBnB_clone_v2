#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import local, runs_once
from datetime import datetime
import os


@runs_once
def do_pack():
    """Archiving the static files"""
    now = datetime.now()
    formatted_time = now.strftime("%Y%m%d%H%M%S")
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    archive_name = "web_static_{}.tgz".format(formatted_time)
    try:
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))
        size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, size))
    except Exception:
        archive_name = None
    return archive_name

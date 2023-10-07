#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


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

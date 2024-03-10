#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive from contents
of the web_static folder"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    archives contents of web_static
    """
    #create versions folder if it does not exist
    local("mkdir -p versions")

    #create the name of the archive file
    time_format = "%Y%m%d%H%M%S"
    archive_name = "versions/web_static_" + datetime.now().strftime(time_format) + ".tgz"

    #compress the web_static folder into a .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_name))

    #check if the compression was successful
    if result.failed:
        return None
    else:
        return archive_name

if __name__ == "__main__":
    do_pack()

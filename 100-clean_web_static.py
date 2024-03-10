#!/usr/bin/python3
""" A Fabric script that deletes out-of-date archives"""

from fabric.api import *
from datetime import datetime

env.hosts = ['54.165.3.212', '100.24.235.18']


def do_clean(number=0):
    """
    cleans out-of-date archives
    """
    number = int(number) if int(number) != 0 else 1
    local_archives = sorted(os.listdir("versions"))
    [local_archives.pop() for a in range(number)]
    with lcd("versions"):
        for archive in local_archives:
            local("rm /{}".format(archive))
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -t").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        [remote_archives.pop() for i in range(number)]
        for archive in remote_archives:
            run("rm -rf ./{}".format(archive))

#!/usr/bin/python3
""" A Fabric script that deletes out-of-date archives"""

from fabric.api import *
from datetime import datetime

env.hosts = ['54.165.3.212', '100.24.235.18']


def do_clean(number=0):
    """
    cleans out-of-date archives
    """
    try:
        number = int(number)
        if number < 0:
            number = 0
        with lcd("versions"):
            local("ls -t | tail -n +{} | xargs -I {{}} rm {{}}"
                    .format(number + 1))
        with cd("/data/web_static/releases"):
            run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}"
                    .format(number + 1))
        return True
    except:
        return False


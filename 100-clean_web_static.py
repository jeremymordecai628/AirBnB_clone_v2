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
        local_archives = sorted(os.listdir("versions"), key=os.path.getctime, reverse=True)
        for archive in local_archives[number:]:
            local(f"rm versions/{archives}")
        with cd("/data/web_static/releases"):
            remote_archives = run("ls -t").split()
            for archive in remote_archives[number:]:
                run(f"rm -rf {archive}")
        return True
    except Exception as e:
        print(f"An error occured: {e}")
        return False

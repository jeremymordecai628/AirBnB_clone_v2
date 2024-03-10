#!/usr/bin/python3
""" The Fabric script distributes an archive to my servers"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.165.3.212-web-01', '100.24.235.18-web-02']
env.user = "ubuntu"


def do_pack():
    """
    archives contents of web_static
    """
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    date_time = datetime.now().strftime(time_format)
    archive_name = "versions/web_static_" + date_time + ".tgz"

    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.failed:
        return None
    else:
        return archive_name


def do_deploy(archive_path):
    """
    Distributes an arcchive to my web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        filename = os.path.basename(archive_path)
        archive_folder = "/data/web_static/releases/{}".format(
                                                        filename.split(".")[0])
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(filename, archive_folder))
        run('mv {}/web_static/* {}'.format(archive_folder, archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln {} /data/web_static/current'.format(archive_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
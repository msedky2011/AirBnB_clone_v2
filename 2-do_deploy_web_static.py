#!/usr/bin/python3
"""Python module to deploy archive on web servers"""
from os import path

from fabric.api import env, put, run

env.hosts = ["18.206.207.38", "3.86.7.50"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """Deploy web files to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, "/tmp/")

        timestamp = archive_path[-18:-4]
        run(
            "sudo mkdir -p /data/web_static/\
releases/web_static_{}/".format(
                timestamp
            )
        )

        run(
            "sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/".format(
                timestamp, timestamp
            )
        )

        run("sudo rm /tmp/web_static_{}.tgz".format(timestamp))

        run(
            "sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/".format(
                timestamp, timestamp
            )
        )

        run(
            "sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static".format(
                timestamp
            )
        )

        run("sudo rm -rf /data/web_static/current")

        run(
            "sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current".format(
                timestamp
            )
        )
    except:
        return False

    return True

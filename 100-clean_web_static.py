#!/usr/bin/python3
"""A module that deletes old archives"""
import os

from fabric.api import cd, env, lcd, local, run

env.hosts = ["18.206.207.38", "3.86.7.50"]


def do_clean(number=0):
    """A function that deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

#!/usr/bin/python3
"""do_clean funtion"""
from fabric import *
import os


def do_clean(number=0):
    """do clean funtion"""
    try:
        number = int(number)
        if number > 1:
            local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))
            run("ls -1t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} sudo rm -rf /data/web_static/releases/{{}}".format(number + 1))
            print("Cleaned archives successfully!")
            return True
    else:
        return False
    except Exception as e:
        print("Error:", e)
        return False

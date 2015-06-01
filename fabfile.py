# -*- coding: utf-8 -*-
from fabric.api import *
from datetime import datetime
import sys

env.user = 'joerg'
env.timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')


def do_something():
    """ update instance "something" on server "somewhere" """
    env.hosts = ['somewhere']
    env.deploy_cfg = 'deploy-something.cfg'
    env.targetProjectDir = 'Instances/Something'


def _check_settings():
    if not getattr(env, 'deploy_cfg', None):
        print("\n\n----> Invalid deploy settings\n\n")
        sys.exit(0)


def transfer():
    """ transfer buildout configs and src """
    _check_settings()

    transfer_buildout()
    transfer_src()


def transfer_src():
    """ transfer src """
    _check_settings()

    local("tar hzcfv src.tar.gz src")
    put("src.tar.gz", "%(targetProjectDir)s/src.%(timestamp)s.tar.gz" % (env))
    run("rm -rf %(targetProjectDir)s/src" % (env))
    run("cd %(targetProjectDir)s; tar xzf src.%(timestamp)s.tar.gz" % (env))


def transfer_buildout():
    """ transfer buildout stuff """
    _check_settings()

    run('mkdir -p %(targetProjectDir)s' % (env))

    put("base.cfg", "%(targetProjectDir)s/base.cfg" % (env))
    put("deploy-base.cfg", "%(targetProjectDir)s/deploy-base.cfg" % (env))
    put("buildout.cfg", "%(targetProjectDir)s/buildout.cfg" % (env))
    put("%(deploy_cfg)s" % (env), "%(targetProjectDir)s/deploy.cfg" % (env))

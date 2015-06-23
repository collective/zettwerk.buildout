# zettwerk.buildout
Enhanced template buildout configurations for development and deployment.

# Features

* Development environment
 * plone.api
 * bobtemptlates.plone
 * Products.PrintingMailhost
 * Products.PDBDebugMode
 * collective.profiler
 * zettwerk.i18nduder
 * fabric
 * collective.xmltestreport
 * mr.developer enabled
 * collective.recipe.omelette
 * plone.reload
 * grip installed: to preview markdown based text files

* Deployment environment
 * missingbits + mr.scripty: set the numbers of instances by one setting
 * zeoserver
 * pound
 * supervisor


# Note

One neat thing in this buildout templates is the possiblilty to change the number of needed instances by just one setting. So if you want to have 4 instances, used by pound, just enter the number 4. If you need 10 instances enter the number 10 (via the backends setting in the [config] part).

# First: clone the repository to your local filesystem

    git clone git@github.com:collective/zettwerk.buildout.git


# Setup your new buildout/project root:

    cd zettwerk.build
    git checkout-index -f -a --prefix=/path/to/your/project/

_Be sure to enter the last path separator!_

Enable virtualenv and install zc.buildout (we are not using bootstrap any more, see https://community.plone.org/t/not-using-bootstrap-py-as-default/620)

    cd /path/to/your/project/
    virtualenv .
    ./bin/pip install zc.buildout

# Usecase: setup development environment

Run bootstrap with the develop.cfg

    ./bin/buildout -c develop.cfg

# Usecase: Deployment with a single instance

* copy deploy-single.cfg to deploy.cfg
* change it as you need
* change fabfile as you need
* deploy via ./bin/fabric deploy_something

# Usecase: Deployment with multiple instances

* copy deploy-multi.cfg to deploy.cfg
* change the number of instances if needed
* change fabfile as you need
* deploy via ./bin/fabric deploy_something

# Todos:
* zest.releaser
* replace pound with haproxy
* more examples and documentation

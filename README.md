# zettwerk.buildout
Enhanced template buildout configurations for development and deployment.

# Features

* Included batteries
 * plone.api
 * bobtemptlates.plone
 * Products.PrintingMailhost
 * Products.PDBDebugMode
 * collective.profiler
 * zettwerk.i18nduder
 * fabric
 * collective.xmltestreport
 * missingbits (adapted to work with current buildout versions)
 * mr.developer enabled
 * collective.recipe.omelette
 * plone.reload


# Structure

One neat thing in this buildout templates is the possiblilty to change the number of needed instances by just one setting. So if you want to have 4 instances, used by pound, just enter the number 4. If you need 10 instances enter the number 10 (via the backends setting in the [config] part).

# Example: Development environment

Export or clone the Repository to your local filesystem

    git clone git@github.com:collective/zettwerk.buildout.git
    cd zettwerk.buildout

Enable virtualenv and install zc.buildout (we are not using bootstrap any more, see https://community.plone.org/t/not-using-bootstrap-py-as-default/620)

    virtualenv .
    ./bin/pip install zc.buildout

Run bootstrap with the develop.cfg

    ./bin/buildout -c develop.cfg


# Example: Deployment with a single instance

* copy deploy-single.cfg to deploy.cfg
* change it as you need
* change fabfile as you need
* deploy via ./bin/fabric deploy_something


# Example: Deployment with multiple instances

* copy deploy-multi.cfg to deploy.cfg
* change the number of instances if needed
* change fabfile as you need
* deploy via ./bin/fabric deploy_something


# Todos:
* zest.releaser
* code quality stuff

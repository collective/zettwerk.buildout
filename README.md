# zettwerk.buildout
Enhanced template buildout configurations for development and deployment.

# Features

* Included batteries
** plone.api
** bobtemptlates.plone
** Products.PrintingMailhost
** Products.PDBDebugMode
** collective.profiler
** zettwerk.i18nduder
** fabric
** collective.xmltestreport
** missingbits (adapted to work with current buildout versions)
** mr.developer enabled
** collective.recipe.omelette
** plone.reload

todo: zest.releaser
todo: code quality stuff
todo: pdbdebugmode

# Structure

# Example: Development environment

* Export or clone the Repository to your local filesystem
> git clone git@github.com:collective/zettwerk.buildout.git
> cd zettwerk.buildout

* enable virtualenv and install zc.buildout (we are not using bootstrap any more, see https://community.plone.org/t/not-using-bootstrap-py-as-default/620)
> virtualenv .
> ./bin/pip install zc.buildout

# run bootstrap with the develop.cfg
> ./bin/buildout -c develop.cfg

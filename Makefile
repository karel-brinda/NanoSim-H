sPHONY: \
	all nanosim-h clean install \
	test \
	pylint flake8 yapf \
	inc pypi sha256 \
	docs readme wpypi wconda \
	help

PIP=/usr/bin/env pip
PYTHON=/usr/bin/env python3

ROOT_DIR = $(shell pwd)

###############
# BASIC RULES #
###############

all:

help: ## Print help message
	    @echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s : | sort)"

clean: ## Clean
	$(PYTHON) setup.py clean --all
	$(MAKE) -C tests clean

install: ## Install nanosim-h using PIP
install:
	$(PIP) uninstall -y nanosim-h || true
	$(PIP) install .


###########
# TESTING #
###########

test: test_repo

test_repo: ## Run unit tests & integration from the repo dir
test_repo:
	$(MAKE) -C tests clean
	$(MAKE) -C tests

pylint: ## Run PyLint
	$(PYTHON) -m pylint nanosimh

flake8: ## Run Flake8
	flake8

yapf: ## Run YAPF (inline replacement)
	yapf -i --recursive nanosimh setup.py tests


#############
# RELEASING #
#############

inc: ## Increment version
inc:
	./nanosimh/increment_version.py

pypi: ## Upload nanosim-h to PyPI
pypi:
	$(MAKE) clean
	$(PYTHON) setup.py sdist bdist_wheel upload

sha256: ## Compute sha256 for the PyPI package
sha256:
	s=$$(curl https://pypi.python.org/pypi/nanosim-h  2>/dev/null| perl -pe 's/#/\n/g' | grep -o 'https.*\.tar\.gz' | xargs curl -L 2>/dev/null | shasum -a 256 | awk '{print $$1;}'); echo $$s; echo $$s | pbcopy


#######################
# DOCUMENTATION & WEB #
#######################


readme: ## Convert README to HTML
readme:
	./update_readme_cli.py
	rst2html.py README.rst > README.html

wconda: ## Open nanosim-h Bioconda webpage
	open https://bioconda.github.io/recipes/nanosim-h/README.html

wpypi: ## Open nanosim-h PyPI webpage
	open https://pypi.python.org/pypi/nanosim-h


WWWDIR = ../www
BINDIR = ../bin
VIRTUAL_ENV = env
LOCAL_PY = $(shell pwd)/local-py

all: virtual

# one solution that works on hubzero
# give a full path to virtualenv command

#virtual:
#	@echo "--> Setup and activate virtualenv"
#	cd ${WWWDIR}; \
#	if test ! -d "$(VIRTUAL_ENV)"; then \
#	  pip install --user virtualenv; \
#	  ~/.local/bin/virtualenv --no-site-packages $(VIRTUAL_ENV); \
#	  . $(VIRTUAL_ENV)/bin/activate; \
#	  pip install -r requirements.txt; \
#	  deactivate; \
#	fi
#	@echo ""


# a version that will probably work for most peopl
# install virtualenv with --user flag
# virtualenv should be in the path,
# (as long as ~/.login is in the path), right?

#virtual:
#	@echo "--> Setup and activate virtualenv"
#	cd ${WWWDIR}; \
#	if test ! -d "$(VIRTUAL_ENV)"; then \
#	  pip install --user virtualenv; \
#	  virtualenv --no-site-packages $(VIRTUAL_ENV); \
#	  . $(VIRTUAL_ENV)/bin/activate; \
#	  pip install -r requirements.txt; \
#	  deactivate; \
#	fi
#	@echo ""


# probably the most contained install
# install virtualenv in a local-py directory
# add local-py/lib/python2.7/site-packages

virtual:
	@echo "--> Setup and activate virtualenv"
	if test ! -d "$(LOCAL_PY)"; then \
	  pip install --install-option="--prefix=$(LOCAL_PY)" --ignore-installed virtualenv; \
	fi; \
	if test ! -d "${WWWDIR}/$(VIRTUAL_ENV)"; then \
	  PY_VERSION_MM=`python --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1-2`; \
	  export PYTHONPATH=${LOCAL_PY}/lib/python$${PY_VERSION_MM}/site-packages:${PYTHONPATH}; \
	  $(LOCAL_PY)/bin/virtualenv ${WWWDIR}/$(VIRTUAL_ENV); \
	  . ${WWWDIR}/$(VIRTUAL_ENV)/bin/activate; \
	  pip install -r $(WWWDIR)/requirements.txt; \
	  deactivate; \
	fi
	@echo ""


install: virtual
	install -D --mode 0755 run_flask.sh ${BINDIR}/run_flask.sh

clean:

distclean: clean
	rm -rf ${WWWDIR}/env \
	       ${BINDIR}/run_flask.sh;
	find ${WWWDIR} -name *.pyc -exec rm {} +
